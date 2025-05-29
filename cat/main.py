import os

ROOT_DIR = os.path.abspath(r"C:\Users\Public\Droid-OS\root")

def is_within_root(path):
    abs_path = os.path.abspath(path)
    return abs_path.startswith(ROOT_DIR)

def run():
    file_name = input("Enter the filename to view: ").strip()
    file_path = os.path.abspath(os.path.join(os.getcwd(), file_name))

    if not is_within_root(file_path):
        print("Access denied: cannot read outside root.")
        return

    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            print("\n" + "="*40)
            print(file.read())
            print("="*40 + "\n")
    except Exception as e:
        print(f"Error reading file: {e}")
