import getpass
from crypto_utils import derive_key
from storage import load_salt, load_vault, save_vault


def verify_master_password(original_key, salt):
    """
    Re-verify master password before sensitive actions
    """
    password = getpass.getpass("Re-enter master password: ")
    test_key = derive_key(password, salt)
    return test_key == original_key


def main():
    print("Local Password Manager")

    # Initial authentication
    master_password = getpass.getpass("Master password: ")
    salt = load_salt()
    key = derive_key(master_password, salt)

    try:
        vault = load_vault(key)
    except Exception:
        print("Wrong master password or corrupted vault.")
        return

    while True:
        print("\n===== MENU =====")
        print("1. Add password")
        print("2. View password")
        print("3. Delete password")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        # ADD PASSWORD
        if choice == "1":
            service = input("Service name: ").strip().lower()
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")

            # Save the new password in the vault
            vault[service] = {
                "username": username,
                "password": password
            }

            save_vault(vault, key)
            print("Password saved successfully.")

        # VIEW PASSWORD
        elif choice == "2":
            if not verify_master_password(key, salt):
                print("Wrong master password.")
                continue

            service = input("Service name: ").strip().lower()
            if service in vault:
                print(f"Username: {vault[service]['username']}")
                print(f"Password: {vault[service]['password']}")
            else:
                print("Service not found.")

        # DELETE PASSWORD
        elif choice == "3":
            if not verify_master_password(key, salt):
                print("Wrong master password.")
                continue

            service = input("Service name: ").strip().lower()
            if service in vault:
                del vault[service]  # Remove the service from the vault
                save_vault(vault, key)
                print("Password deleted successfully.")
            else:
                print("Service not found.")

        # EXIT
        elif choice == "4":
            print("Exiting password manager.")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
    main()
