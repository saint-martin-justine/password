import hashlib

def check_password(password):

    if len(password) < 8:
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    if not any(char in special_chars for char in password):
        return False
    
    return True

def encrypt_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def main():
    while True:
        password = input("Veuillez entrer votre mot de passe : ")
        
        if check_password(password):
            hashed_password = encrypt_password(password)
            print("Mot de passe valide.")
            print("Mot de passe crypté :", hashed_password)
            break
        else:
            print("Mot de passe invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()