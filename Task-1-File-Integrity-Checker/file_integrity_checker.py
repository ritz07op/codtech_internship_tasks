# Task-1-File-Integrity-Checker
import hashlib
import os


def calculate_file_hash(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        return hashlib.sha256(content).hexdigest()


def check_file_integrity(original_hash, file_path):
    current_hash = calculate_file_hash(file_path)
    return original_hash == current_hash


if __name__ == "__main__":
    file = input("Enter file path: ")
    if os.path.exists(file):
        original = calculate_file_hash(file)
        print(f"Original Hash: {original}")

        input("\nMake changes to the file if you want and press Enter to recheck...\n")

        if check_file_integrity(original, file):
            print("\n✅ File is intact.")
        else:
            print("\n⚠️ File has been modified!")
    else:
        print("File not found.")

