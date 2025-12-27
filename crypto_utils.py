# Import base64 for encoding the derived key
import base64
# Import os for operating system operations (currently unused)
# import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Derive an encryption key from a password using PBKDF2-HMAC-SHA256
def derive_key(password: str, salt: bytes) -> bytes:
    # Initialize PBKDF2 with SHA256 algorithm
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes = 256 bits
        salt=salt,  # Random salt for key derivation
        iterations=100000,  # Number of iterations for security
    )
    # Derive and return base64-encoded key
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Encrypt data using Fernet (symmetric encryption)
def encrypt_data(data: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(data)

# Decrypt data using Fernet
def decrypt_data(data: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(data)
