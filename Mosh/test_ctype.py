import ctypes

lib = ctypes.cdll.LoadLibrary("libwrapctype.dll")
lib.hello()

