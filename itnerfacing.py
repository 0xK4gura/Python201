from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL

MessageBoxA = windll.user32.MessageBoxA #What library it called from; it is User32.dll but we put user32 since we called windll in front
MessageBoxA.argtypes =(HWND, LPCSTR, LPCSTR, UINT) #What arguements it take
MessageBoxA.restype = INT #Return Function 

print(MessageBoxA)

# Parameters for a MessageBoxA function 

lpText = LPCSTR(b"World") # from msdn documentation
lpCaption =LPCSTR(b"Hello")
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001

# MessageBoxA(None, lpText, lpCaption, MB_OKCANCEL)

GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = INT

# buffer_size = DWORD(2)
# buffer = create_string_buffer(buffer_size.value)

# GetUserNameA(buffer, byref(buffer_size))
# print(buffer.value)

# error = GetLastError()

# if error: # buffer_size 2 produce error 122 by navigating error code 122 msdn: system error code: Error_Insufficient_Buffer
# 	print(error)
# 	print(WinError(error))

# GetWindowRect Function
# Since it is expecting lpRect and HWND

class RECT(Structure):
	_fields_ = [("left", c_long),
				("top", c_long),
				("right", c_long),
				("bottom", c_long)]

rect = RECT()

# print(rect.left)
# print(rect.top)
# print(rect.right)
# print(rect.bottom)

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE, POINTER(RECT))
GetWindowRect.restype = BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))
# produce the dimensions of the current window
print("Left Dimensions: ", rect.left)
print("Top Dimensions: ", rect.top)
print("Right Dimensions: ", rect.right)
print("Bottom Dimensions: ",rect.bottom)


