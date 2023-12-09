import time
import os

args = ""
patch_target = ""

os.system("./patcher/patcher" + patch_target + "--logd-compatibility " + args)

if (args == "") :
    print("arguments cannot be empty. You must select a patching mode")
else :
    pass

if (patch_target == "") :
    print("Your patch target cannot be empty")