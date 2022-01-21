from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID # pointer to avoid object

	#lpAddress -- starting address of the region to allocate
	#dwSize -- size of the region in byte
	#flAllocationType -- type of memory allocation
MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000

	#flProtect -- memory protection for the region of pages to be allocated
PAGE_EXECUTE_READWRITE = 0x40

ptr = VirtualAlloc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
error = GetLastError()

if error:
	print(error)
	print(WinErorr(error))

print("VirtualAlloc: ", hex(ptr))

nt = windll.ntdll
NTSTATUS = wintypes.DWORD

NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
NtAllocateVirtualMemory.restype = NTSTATUS

# now we know how function is defined, we need to understand how we can interact

#ProcessHandle mapping should be done -- GetCurrentProcess function = pseudohandle
handle = 0xffffffffffffffff

#BaseAddress - A pointer to a variable which receive the base address
base_address = wintypes.LPVOID(0x0)

#Zerobits 
zero_bits = wintypes.ULONG(0)

#RegionSize - receive the actual size allocated region of pages in byte
size = wintypes.ULONG(1024 * 12) # big to observe

ptr2 = NtAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr2 != 0:
	print("error!")
	print(ptr2)

print("NtAllocateVirtualMemory: ", hex(base_address.value))


input()






