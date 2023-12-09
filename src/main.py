print("\nIntelliPatcher")
print("by StNiosem\n")

error_code = "success"
error_value = 0
lib_count = 0

programName = "DefaultProgram"
programPID = 12345

print("Importing libraries.\n")

# Libraries
import time; print("Imported time for timers"); lib_count +=1; time.sleep(0.05)
from password_maker import generate; print("Imported password_maker for UUIDs"); lib_count += 1; time.sleep(0.25)
import fileinput; print("Imported fileinput for inputting patches"); lib_count += 1; time.sleep(0.5)
import os; print("Imported os for system calls"); lib_count += 1; time.sleep(0.35)
import psutil; print("Imported psutil for reading RAM"); lib_count += 1; time.sleep(0.5)
import patcher; print("Imported local package patcher for patching"); lib_count += 1; time.sleep(0.125)
import logd; print("Imported local package logd for custom patch log events"); lib_count += 1; time.sleep(0.1)

# Define memory values
memoryResult = "Memory exists"

# Check lib_count for values. Employ plural form if needed. Esle it displays error that value
# isn't in the explected range (0 and up) and exit

if (lib_count == 0) :
    print("\nImported no libraries.")
elif (lib_count == 1) :
    print("\nImported " + str(lib_count) + " Library")
elif (lib_count > 1) :
    print("\nImported " + str(lib_count) + " Libraries")
else :
    error_code = "org.ferrytelabs.fera.unexpected_value"
    error_value = -11
    print("\nUnexpected value in int lib_count (lib_count = " + str(lib_count) + "). Exiting with error code \"" + error_code +"\" (" + str(error_value) +")")
    exit()

def memory_read() :
    print("\nReading Memory for Program")
    time.sleep(4)
    print("\nYour computer has memory : " + memoryResult + "\n")
    return 0