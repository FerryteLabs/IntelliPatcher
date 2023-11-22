print("\nIntelliPatcher")
print("by StNiosem\n\n")

lib_count = 0

print("Importing libraries.")
from password_maker import generate; print("Importing password_maker for UUIDs"); lib_count += 1

if (lib_count == 0) :
    print("Imported no libraries.")

elif (lib_count == 1) :
    print("\nImported " + str(lib_count) + " Library")

elif (lib_count > 1) :
    print("\nImported " + str(lib_count) + " Libraries")

else :
    print("unexpected value in counter lib_count")