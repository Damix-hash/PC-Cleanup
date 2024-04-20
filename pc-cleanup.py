import os
from os import system
import shutil

system("title " + "PC-Cleanup")

#     ___   _____       _____   __
#    / _ \ / ___/ ____ / ___/  / / ___  ___ _  ___  __ __   ___
#   / ___// /__  /___// /__   / / / -_)/ _ `/ / _ \/ // /  / _ \
#  /_/    \___/       \___/  /_/  \__/ \_,_/ /_//_/\_,_/  / .__/
#                                                        /_/


def warn():
    print()
    print("WARNING!")
    print("PC-CLEANUP.PY REMOVES TEMPORARY/CACHE FILES FROM YOUR DEVICE")
    print("MAKE SURE YOU HAVE NO APPLICATIONS RUNNING FOR THE BEST RESULTS!")
    print()
    print("SINCE IT REMOVES FILES FROM THOSE FOLDERS YOU SHOULD CHECK IF YOU GOT")
    print("NOTHING IMPORTANT SAVED THERE (ignoring you shouldn't have anything important in those folders.")
    print()


banner = (
     """
               ___   _____       _____   __                              
              / _ \\ / ___/ ____ / ___/  / / ___  ___ _  ___  __ __   ___ 
             / ___// /__  /___// /__   / / / -_)/ _ `/ / _ \\/ // /  / _ \\
            /_/    \\___/       \\___/  /_/  \\__/ \\_,_/ /_//_/\\_,_/  / .__/
                                                                  /_/    
"""
)

seperator = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print(banner)
print(seperator)
warn()
print(seperator)
print()
input(f"Press ENTER To Continue... \n\n{seperator}")
print()

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")

# Clearing CACHE For Your Own Safety!
# You never know if you have anything illegal in cache.
# EVERY SINGLE IMAGE THAT LOADS ON ANY SITE SAVES TO CACHE

PATHS = {
    "Temp": LOCAL + "\\Temp",
    "Discord Cache": ROAMING + "\\Discord\\Cache",
    "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default\\Cache",
    "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache",
    "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default\\Cache",
    "Chromium": LOCAL + "\\Chromium\\User Data\\Default\\Cache",
    "Opera": LOCAL + "\\Opera Software\\Opera Stable\\Cache",
    "Opera GX": ROAMING + "\\Opera Software\\Opera GX Stable\\Cache",
    "UC Browser": LOCAL + "\\UCBrowser\\User Data\\Default\\Cache",
    "Maxthon": LOCAL + "\\Maxthon3\\Temp\\~MxCache\\Cache",
}

CLEANED_MEMORY = 0

def remove_all(folder):
    global CLEANED_MEMORY
    
    folder = str(folder)

    if os.path.exists(folder):
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path):
                try:
                    MEMORY = os.path.getsize(file_path)
                    os.remove(file_path)
                    CLEANED_MEMORY += MEMORY
                except Exception as file_err:
                    print("Error With Removing File: ", file_err)
            elif os.path.isdir(file_path):
                try:
                    shutil.rmtree(file_path)
                    if os.path.exists(file_path):
                        os.rmdir(file_path)  # i dont know i just wanted to add it for no reason honestly
                except Exception as dir_err:
                    print("Error With Removing Directory: ", dir_err)
    else:
        print(f"Folder does not exist: {folder}")


def main():
    for path in PATHS.values():
        remove_all(path)


main()
print()
print(seperator)
print()
print("Finished Removing Your Temp Files!")
print("Logs:")
print(f"REMOVED {CLEANED_MEMORY/1048576} BYTES FROM YOUR WINDOWS DEVICE")
input("Press ENTER To Leave...")
