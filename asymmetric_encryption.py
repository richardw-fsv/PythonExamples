import rsa
import base64

def generate_keys() -> tuple[str, str]:
    """
    Generates a pair of RSA keys (public and private).

    Returns
        Tuple: A tuple containing the public key and private key.
    """
    (public_key, private_key) = rsa.newkeys(2048)
    base64_public_key = base64.b64encode(public_key.save_pkcs1()).decode()
    base64_private_key = base64.b64encode(private_key.save_pkcs1()).decode()
    print(f"Generated RSA keys (Base64):\nPublic Key:\n{base64_public_key}\nPrivate Key:\n{base64_private_key}")
    return base64_public_key, base64_private_key

def encrypt(message: str, public_key: str) -> str:
    """
    Encrypts a message using the provided RSA public key.

    Args
        message (str): The plaintext message to be encrypted.
        public_key (str): The RSA public key used for encryption, encoded in Base64 format.

    Returns
        String: The encrypted message encoded in Base64 format for easier storage and transmission.
    """
    rsa_public_key = rsa.PublicKey.load_pkcs1(base64.b64decode(public_key))
    encrypted_message = rsa.encrypt(message.encode(), rsa_public_key)
    return base64.b64encode(encrypted_message).decode()

def decrypt(encrypted_message: str, private_key: str) -> str:
    """
    Decrypts a message using the provided RSA private key.

    Args
        encrypted_message (str): The encrypted message to be decrypted, encoded in Base64 format.
        private_key (str): The RSA private key used for decryption, encoded in Base64 format.

    Returns
        String: The decrypted message.
    """
    rsa_private_key = rsa.PrivateKey.load_pkcs1(base64.b64decode(private_key))
    decrypted_message = rsa.decrypt(base64.b64decode(encrypted_message), rsa_private_key)
    return decrypted_message.decode()


# Asymmetric encryption example using RSA
print("Asymmetric Encryption Example using RSA in Python")  
public_key, private_key = generate_keys()

message:str = "This is a secret message that needs to be encrypted."
print(f"Original message: {message}")

encrypted_message:str = encrypt(message, public_key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message:str = decrypt(encrypted_message, private_key)
print(f"Decrypted message: {decrypted_message}")