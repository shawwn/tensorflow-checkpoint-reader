from typing import Any, Callable, Union

def putattr(self: Any, name: str, create: Callable):
  if not hasattr(self, name):
    setattr(self, name, create())
  return getattr(self, name)
