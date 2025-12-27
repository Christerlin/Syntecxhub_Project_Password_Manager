import json
import os
from crypto_utils import encrypt_data, decrypt_data

# File paths for encrypted vault and salt storage
DATA_FILE = "vault.dat"
SALT_FILE = "salt.bin"

def load_salt():
    """Load salt from file, or generate and save a new one if it doesn't exist."""
    if not os.path.exists(SALT_FILE):
        # Generate a random 16-byte salt
        salt = os.urandom(16)
        # Save salt to file
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        # Read existing salt from file
        with open(SALT_FILE, "rb") as f:
            salt = f.read()
    return salt

def save_vault(data: dict, key: bytes):
    """Encrypt and save vault data to file."""
    # Convert dict to JSON string, then to bytes, and encrypt
    encrypted = encrypt_data(json.dumps(data).encode(), key)
    # Write encrypted data to file
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def load_vault(key: bytes) -> dict:
    """Load and decrypt vault data from file, return empty dict if file doesn't exist."""
    # Return empty dict if vault file doesn't exist
    if not os.path.exists(DATA_FILE):
        return {}
    # Read encrypted data from file
    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()
    # Decrypt data and convert back to dict
    decrypted = decrypt_data(encrypted, key)
    return json.loads(decrypted.decode())
