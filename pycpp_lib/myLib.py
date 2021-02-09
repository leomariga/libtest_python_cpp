import ctypes
import sys
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

# mylib_core is the .so or .dll as a cross-platform name
#handle = ctypes.CDLL(dir_path + "/mylib_core")     

#handle.My_Function.argtypes = [ctypes.c_int] 
  
def My_Function(num):
    #return handle.My_Function(num)   
    return 2