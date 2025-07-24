from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"✅ File encrypted: {filename}.enc")

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    decrypted_filename = "decrypted_" + os.path.basename(filename).replace(".enc", "")
    with open(decrypted_filename, "wb") as file:
        file.write(decrypted)
    print(f"✅ File decrypted: {decrypted_filename}")

if __name__ == "__main__":
    print("=== Advanced File Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").lower()

    if choice == 'e':
        filepath = input("Enter the path of the file to encrypt: ").strip()
        if os.path.exists(filepath):
            key = generate_key()
            encrypt_file(filepath, key)
            print("🔑 Key saved as secret.key")
        else:
            print("❌ File not found.")
    
    elif choice == 'd':
        filepath = input("Enter the path of the encrypted (.enc) file: ").strip()
        if os.path.exists("secret.key") and os.path.exists(filepath):
            key = load_key()
            decrypt_file(filepath, key)
        else:
            print("❌ File or secret.key missing.")
    else:
        print("❌ Invalid option.")

