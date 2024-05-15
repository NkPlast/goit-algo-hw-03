import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    try:
        # Створення вихідної директорії, якщо вона не існує
        os.makedirs(dest_dir, exist_ok=True)

        # Обхід файлів та піддиректорій у вихідній директорії
        for item in os.listdir(source_dir):
            path = os.path.join(source_dir, item)
            if os.path.isdir(path):
                # Рекурсивний виклик, якщо елемент є директорією
                copy_files(path, dest_dir)
            elif os.path.isfile(path):
                # Визначення розширення файлу
                ext = os.path.splitext(item)[1][1:].lower()
                if ext == "":
                    ext = "no_extension"
                
                # Створення піддиректорії на основі розширення файлу
                ext_dir = os.path.join(dest_dir, ext)
                os.makedirs(ext_dir, exist_ok=True)
                
                # Копіювання файлу
                shutil.copy2(path, ext_dir)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the source directory.")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"
    
    copy_files(source_directory, destination_directory)
    print("Files have been successfully copied and sorted by extension.")
