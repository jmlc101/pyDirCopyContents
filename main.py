import os
import shutil

def main():
    print("\nThis app moves all files contained within a directory into another file or directory.\n")
    sourceIsInput = False
    while (sourceIsInput == False):
        source = input("Enter source directory path...\nEX: /home/user/file/subfile/\n")
        if (source[len(source)-1]) != '/':
            print("\nPlease try again, path must end with forward-slash '/'...")
        elif (source[len(source)-1]) == '/':
            sourceIsInput = True
    destination = input ("\nEnter destination file path...\n")

    files = os.listdir(source)

    for f in files:
        shutil.move(source+f, destination)

if __name__ == "__main__":
    main()