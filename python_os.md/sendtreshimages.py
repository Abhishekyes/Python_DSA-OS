import os
import shutil
from PIL import Image

def main():
    TARGET_dir = "img"

    os.chdir(TARGET_dir)

    files = os.listdir(".")

    os.makedirs("Trash", exist_ok=True)

    for file_ in files:
        try:
            Image.open(file_)
        except Exception as e:
            print(f"Error: {e}")
            shutil.move(file_,"Trash")
            print(f"{file_} move to Trash dir")

if __name__ =="__main__":
    main()
