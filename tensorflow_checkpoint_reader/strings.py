from enum import Enum, auto
from typing import Union

from . import core, str_util

# from fifostr import FIFOStr
#
# class string(FIFOStr):
#   def __init__(self, value = ""):
#     super().__init__(2 ** 63 - 1)
#     self.append(value)
#
#   def set(self, value: str):
#     self.clear()
#     self.append(str(value))

def str_cat(*args):
  return ''.join([str(x) for x in args])

def printf(format, *args) -> bytes:
  format = core.string_view(format).bytes()
  format = format.replace(b"%llx", b"%x")
  return format % args

class Ascii:
  LOWER_A = ord('a')
  LOWER_Z = ord('z')
  UPPER_A = ord('A')
  UPPER_Z = ord('Z')
  DIGIT_0 = ord('0')
  DIGIT_9 = ord('9')
  DOT = ord('.')
  DASH = ord('-')
  UNDERSCORE = ord('_')
  SLASH = ord('/')
  PLUS = ord('+')
  MINUS = ord('-')
  RANGLE = ord('>')

class Scanner:
  class CharClass(Enum):
    # NOTE: When adding a new CharClass, update the AllCharClasses ScannerTest
    # in scanner_test.cc
    ALL = auto()
    DIGIT = auto()
    LETTER = auto()
    LETTER_DIGIT = auto()
    LETTER_DIGIT_DASH_UNDERSCORE = auto()
    LETTER_DIGIT_DASH_DOT_SLASH = auto()             # SLASH is / only, not backslash
    LETTER_DIGIT_DASH_DOT_SLASH_UNDERSCORE = auto()  # SLASH is / only, not backslash
    LETTER_DIGIT_DOT = auto()
    LETTER_DIGIT_DOT_PLUS_MINUS = auto()
    LETTER_DIGIT_DOT_UNDERSCORE = auto()
    LETTER_DIGIT_UNDERSCORE = auto()
    LOWERLETTER = auto()
    LOWERLETTER_DIGIT = auto()
    LOWERLETTER_DIGIT_UNDERSCORE = auto()
    NON_ZERO_DIGIT = auto()
    SPACE = auto()
    UPPERLETTER = auto()
    RANGLE = auto()

  def __init__(self, source: core.StringPiece):
    self._error = False
    self._capture_start = None
    self._capture_end = None
    self._cur = core.string_view(source)
    self.restart_capture()

  def one(self, clz: CharClass):
    """Consume the next character of the given class from input. If the next
    character is not in the class, then GetResult will ultimately return false."""
    if self._cur.empty() or not self.matches(clz, self._cur[0]):
      return self.error()
    self._cur.remove_prefix(1)
    return self

  def zero_or_one_literal(self, s: core.StringPiece):
    """Consume the next s.size() characters of the input, if they match <s>. If
    they don't match <s>, this is a no-op."""
    str_util.consume_prefix(self._cur, s)
    return self

  def one_literal(self, s: core.StringPiece):
    """Consume the next s.size() characters of the input, if they match <s>. If
    they don't match <s>, then GetResult will ultimately return false."""
    if not str_util.consume_prefix(self._cur, s):
      self._error = True
    return self

  def any(self, clz: CharClass):
    """Consume characters from the input as long as they match <clz>. Zero
    characters is still considered a match, so it will never cause GetResult to
    return false."""
    while not self._cur.empty() and self.matches(clz, self._cur[0]):
      self._cur.remove_prefix(1)
    return self

  def many(self, clz: CharClass):
    """Shorthand for One(clz).Any(clz)."""
    return self.one(clz).any(clz)

  def restart_capture(self):
    """Reset the capture start point.

    Later, when GetResult is called and if it returns true, the capture
    returned will start at the position at the time this was called."""
    self._capture_start = self._cur.begin()
    self._capture_end = None
    return self

  def stop_capture(self):
    """Stop capturing input.

    Later, when GetResult is called and if it returns true, the capture
    returned will end at the position at the time this was called."""
    self._capture_end = self._cur.begin()
    return self

  def eos(self):
    """If not at the input of input, then get_result will ultimately return false."""
    if not self._cur.empty():
      self._error = True
    return self

  def any_space(self):
    """Shorthand for Any(SPACE)."""
    return self.any(Scanner.CharClass.SPACE)

  def scan_until(self, end_ch):
    """This scans input until <end_ch> is reached. <end_ch> is NOT consumed."""
    self.scan_until_impl(end_ch, escaped=False)
    return self

  def scan_escaped_until(self, end_ch):
    """This scans input until <end_ch> is reached. <end_ch> is NOT consumed.
    Backslash escape sequences are skipped.
    Used for implementing quoted string scanning."""
    self.scan_until_impl(end_ch, escaped=True)
    return self

  def peek(self,default_value = 0):
    """Return the next character that will be scanned, or <default_value> if there
    are no more characters to scan.
    Note that if a scan operation has failed (so GetResult() returns false),
    then the value of Peek may or may not have advanced since the scan
    operation that failed."""
    return default_value if self._cur.empty() else self._cur[0]

  def empty(self) -> bool:
    """Returns false if there are no remaining characters to consume."""
    return self._cur.empty()

  def scan_until_impl(self, end_ch, escaped: bool):
    while True:
      if self._cur.empty():
        self.error()
        return
      ch = self._cur[0]
      if ch == end_ch:
        return

      self._cur.remove_prefix(1)
      if escaped and ch == 92:  # backslash
        # Escape character, skip next character.
        if self._cur.empty():
          self.error()
          return
        self._cur.remove_prefix(1)

  def get_result(self, remaining: core.StringPiece = None, capture: core.StringPiece = None) -> bool:
    """Returns true if the input string successfully matched. When true is
    returned, the remaining string is returned in <remaining> and the captured
    string returned in <capture>, if non-NULL."""
    if self._error:
      return False
    if remaining is not None:
      remaining.set(self._cur)
    if capture is not None:
      end = self._cur.begin() if self._capture_end is None else self._capture_end
      capture.set(core.StringPiece(self._capture_start, end - self._capture_start))
    return True

  def error(self):
    self._error = True
    return self

  @staticmethod
  def is_letter(ch):
    #return 97 <= ch <= 122 or 65 <= ch <= 90  # 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
    return Ascii.LOWER_A <= ch <= Ascii.LOWER_Z or Ascii.UPPER_A <= ch <= Ascii.UPPER_Z

  @staticmethod
  def is_lower_letter(ch):
    # return 97 <= ch <= 122  # 'a' <= ch <= 'z'
    return Ascii.LOWER_A <= ch <= Ascii.LOWER_Z

  @staticmethod
  def is_digit(ch):
    # return 48 <= ch <= 57  # '0' <= ch <= '9'
    return Ascii.DIGIT_0 <= ch <= Ascii.DIGIT_9

  @staticmethod
  def is_space(ch):
    return ch in [32, 9, 10, 11, 12, 13]  # list(map(ord, ' \t\n\v\f\r'))

  @staticmethod
  def matches(clz: CharClass, ch):
    if clz == Scanner.CharClass.ALL:
      return True
    elif clz == Scanner.CharClass.DIGIT:
      return Scanner.is_digit(ch)
    elif clz == Scanner.CharClass.LETTER:
      return Scanner.is_letter(ch)
    elif clz == Scanner.CharClass.LETTER_DIGIT:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch)
    elif clz == Scanner.CharClass.LETTER_DIGIT_DASH_UNDERSCORE:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.DASH or ch == Ascii.UNDERSCORE
    elif clz == Scanner.CharClass.LETTER_DIGIT_DASH_DOT_SLASH:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.DASH or ch == Ascii.DOT or ch == Ascii.SLASH
    elif clz == Scanner.CharClass.LETTER_DIGIT_DASH_DOT_SLASH_UNDERSCORE:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.DASH or ch == Ascii.DOT or ch == Ascii.SLASH or ch == Ascii.UNDERSCORE
    elif clz == Scanner.CharClass.LETTER_DIGIT_DOT:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.DOT
    elif clz == Scanner.CharClass.LETTER_DIGIT_DOT_PLUS_MINUS:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.DOT or ch == Ascii.PLUS or ch == Ascii.MINUS
    elif clz == Scanner.CharClass.LETTER_DIGIT_DOT_UNDERSCORE:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.DOT or ch == Ascii.UNDERSCORE
    elif clz == Scanner.CharClass.LETTER_DIGIT_UNDERSCORE:
      return Scanner.is_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.UNDERSCORE
    elif clz == Scanner.CharClass.LOWERLETTER:
      return Scanner.is_lower_letter(ch)
    elif clz == Scanner.CharClass.LOWERLETTER_DIGIT:
      return Scanner.is_lower_letter(ch) or Scanner.is_digit(ch)
    elif clz == Scanner.CharClass.LOWERLETTER_DIGIT_UNDERSCORE:
      return Scanner.is_lower_letter(ch) or Scanner.is_digit(ch) \
             or ch == Ascii.UNDERSCORE
    elif clz == Scanner.CharClass.NON_ZERO_DIGIT:
      return Scanner.is_digit(ch) and ch != Ascii.DIGIT_0
    elif clz == Scanner.CharClass.SPACE:
      return Scanner.is_space(ch)
    elif clz == Scanner.CharClass.UPPERLETTER:
      return Ascii.UPPER_A <= ch <= Ascii.UPPER_Z
    elif clz == Scanner.CharClass.RANGLE:
      return ch == Ascii.RANGLE
    else:
      return False
