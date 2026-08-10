import io
import sys

from enum import Enum
from types import TracebackType
from typing import Union, Optional, Self

class FileOutModes(Enum):
    APPEND = "a"
    REWRITE = "w"


class FileOut:
    _mode: FileOutModes
    _path_to_file: str
    _orig_stdout: io.TextIOWrapper
    _file: io.TextIOWrapper

    def __init__(
        self,
        path_to_file: str,
        mode: Union[str, FileOutModes] = FileOutModes.REWRITE,
    ) -> None:
        
        self._path_to_file = path_to_file
        if isinstance(mode, FileOutModes):
            self._mode = mode.value
        elif mode in ['w','a']:
            self._mode = mode
        self._orig_stdout = sys.stdout

    def __enter__(self):
        self._file=open(self._path_to_file, self._mode)
        sys.stdout=self._file
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb) -> bool:
        sys.stdout=self._orig_stdout
        self._file.close()
        return False

    @property
    def mode(self) -> FileOutModes:
        return self._mode

    @mode.setter
    def mode(self, mode_new: Union[str, FileOutModes]) -> None:
        if isinstance(mode_new, FileOutModes):
            self._mode = mode_new.value
        elif mode_new in ['w','a']:
            self._mode = mode_new
        else:
            raise ValueError('Mode must be w or a')

#--------------------------------Тесты----------------------------------

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

try:
    file_manager.mode = 'jaja'
except ValueError:
    pass
else:
    assert False