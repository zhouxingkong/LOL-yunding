'''
@date 2013-5-11

Simply implemented errors and wranings classes that do not existed in 
python 2.x and new introduced in python 3.x.

@author Hong-She Liang <starofrainnight@gmail.com>
'''


import sys

if sys.version_info[0] <= 2:
    class BlockingIOError(OSError):
        pass

    class ChildProcessError(OSError):
        pass

    class ChildProcessError(OSError):
        pass

    class ConnectionError(OSError):
        pass

    class BrokenPipeError(ConnectionError):
        pass

    class ConnectionAbortedError(ConnectionError):
        pass

    class ConnectionRefusedError(ConnectionError):
        pass

    class ConnectionResetError(ConnectionError):
        pass

    class FileExistsError(OSError):
        pass

    class FileNotFoundError(OSError):
        pass

    class InterruptedError(OSError):
        pass

    class IsADirectoryError(OSError):
        pass

    class NotADirectoryError(OSError):
        pass

    class PermissionError(OSError):
        pass

    class ProcessLookupError(OSError):
        pass

    class TimeoutError(OSError):
        pass

    class ResourceWarning(Warning):
        pass
