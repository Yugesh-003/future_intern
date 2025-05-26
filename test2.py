import ctypes

try:
    ctypes.cdll.LoadLibrary(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\cudnn64_8.dll")
    print("cuDNN DLL loaded successfully.")
except OSError as e:
    print("Failed to load cuDNN DLL:", e)
