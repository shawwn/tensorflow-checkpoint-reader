from typing import Any, Callable

def putattr(self: Any, name: str, create: Callable):
  if not hasattr(self, name):
    setattr(self, name, create())
  return getattr(self, name)
