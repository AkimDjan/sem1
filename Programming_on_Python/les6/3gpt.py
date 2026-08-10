import io
import sys

from enum import Enum
from types import TracebackType
from typing import Union, Optional, Self

class FileOutModes(Enum):
    APPEND = "a"
    REWRITE = "w"


class FileOut:
    def __init__(
        self,
        path_to_file: str,
        mode: Union[str, FileOutModes] = FileOutModes.REWRITE,
    ) -> None:
        self.path_to_file = path_to_file
        self._mode = mode
        self.original_stdout = None

    @property
    def mode(self) -> FileOutModes:
        if isinstance(self._mode, str):
            return FileOutModes(self._mode)
        else:
            return self._mode

    @mode.setter
    def mode(self, mode_new: Union[str, FileOutModes]) -> None:
        if isinstance(mode_new, str):
            if mode_new not in ("w", "a"):
                raise ValueError(
                    "Invalid mode. Valid modes are 'w' (write) or 'a' (append)."
                )
            self._mode = FileOutModes(mode_new)
        elif isinstance(mode_new, FileOutModes):
            self._mode = mode_new
        else:
            raise TypeError("Invalid mode type. Must be str or FileOutModes.")

    def __enter__(self) -> Self:
        self.file = open(self.path_to_file, self._mode.value)
        self.original_stdout = sys.stdout
        sys.stdout = self.file
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        sys.stdout = self.original_stdout
        self.file.close()
        return False 
    
with FileOut("test.txt") as file_manager:
    print(
        "Hello, World!",
        "This text must be printed into file",
        sep="\n",
    )

print("This text must be printed into stdout")

#---------------------------------------
file_manager.mode = "a"

with file_manager:
    print("Append more text!")

#---------------------------------------
try:
    file_manager.mode = "rewrite"

except ValueError:
    pass

else:
    assert False