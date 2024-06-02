
# Create the environment
Install libraries to run YoLo versions
```
pip install -r requirements.txt
```
Uninstall libraries
```
pip uninstall -r requirements.txt -y
```



# Verify shm.dll file in Pytorch

Init int CMD/Terminal and go
```
1. python
2. import torch
    ERROR
```

If you don't have the file `shm.dll`, you need to go to the next link:
```
  Process:  https://www.youtube.com/watch?v=ca34C8ZUI0A
  Github: https://github.com/pytorch/pytorch/commit/fdfef759a676ee7a853872e347537bc1e4b51390.

Then, copy the code from the link and put it in `init.py`. In the path "C:...." of pytorch packages you can find
the `init.py`.
```
