#Check if WinGet is installed

if (command "winget") {
    winget install python
}
else {
    echo "WinGet isn't installed. Please install it"
    return -2 #WinGet Not Installed
}