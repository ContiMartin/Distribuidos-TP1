from ctypes import *

class Path(Structure):
    _fields_ = [
        ("path", c_wchar_p),
        ("operacion", c_int),
        ]

class PathFiles(Structure):
    _fields_ = [
        ("values", c_wchar_p),
        ]
                
