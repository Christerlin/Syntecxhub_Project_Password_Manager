# Syntecxhub_Project_Password_Manager
A secure local password manager built in Python as part of the Syntecxhub internship program. It encrypts credentials using strong symmetric encryption (AES), derives keys from a master password, and stores data securely on disk

# Local Password Manager – Syntecxhub Internship Project

# Description

This is a secure local password manager built in Python as part of the Syntecxhub internship program.  
It allows users to safely store credentials locally using strong symmetric encryption (AES) and a master password. All sensitive data is encrypted and stored securely on disk.

# Objectives
- Learn secure data storage
- Understand AES encryption and key derivation (PBKDF2)
- Implement master password authentication
- Handle local storage securely using encrypted JSON

# Features
- Add, retrieve, delete credentials for services
- Encrypted vault using AES
- Master password for access control
- Local storage (`vault.dat` + `salt.bin`)
- Passwords never stored in plaintext

# Technologies Used
- Python 3
- cryptography library (Fernet AES)
- JSON for data storage
- getpass for secure input

# Installation
1. Clone the repository:
```bash
git clone https://github.com/Christerlin/Syntecxhub_Project_Password_Manager.git
cd Syntecxhub_Project_Password_Manager

```
# Usage
``` bash
python3 manager.py
```

You will be prompted for a master password.

Menu options:

1.Add password
2.View password
3.Delete password
4.Exit

# Security Notes

All data is encrypted using AES with a key derived from your master password.
Do not share your master password.
Vault and salt files are stored locally.

# Author
Christerlin Joseph
Syntecxhub Internship Program
