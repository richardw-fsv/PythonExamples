import base64

from cryptography.fernet import Fernet

def generateKey() -> str:
    """
    Generates a symmetric key for encryption and decryption.

    Returns
        String: The generated symmetric key encoded in Base64 format for easier storage 
        and transmission.
    """
    key:str = Fernet.generate_key().decode()
    print(f"Generated symmetric key (Base64): {key}")
    return key

def encrypt(message: str, key: str) -> str:
    """
    Encrypts a message using the provided symmetric key.

    Args
        message (str): The plaintext message to be encrypted.
        key (str): The symmetric key used for encryption, encoded in Base64 format.

    Returns
        String: The encrypted message encoded in Base64 format for easier storage and transmission.
    """
    fernet: Fernet = Fernet(key.encode())
    return fernet.encrypt(message.encode()).decode()

def decrypt(encrypted_message: str, key: str) -> str:
    """
    Decrypts a message using the provided symmetric key.

    Args
        encrypted_message (str): The encrypted message to be decrypted, encoded in Base64 format.
        key (str): The symmetric key used for decryption, encoded in Base64 format.

    Returns
        String: The decrypted message.
    """
    fernet: Fernet = Fernet(key.encode())
    return fernet.decrypt(encrypted_message.encode()).decode()


print("Symmetric Encryption Example using Fernet (AES) in Python")
key:str = generateKey()

message:str = "This is a secret message that needs to be encrypted."
print(f"Original message: {message}")

encrypted_message:str = encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message:str = decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")


