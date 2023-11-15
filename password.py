def validar_password(password):
    # Comprueba si el password tiene al menos 8 caracteres
    if len(password) < 8:
        return False
    
    # Comprueba si el password contiene solo números y letras
    if not password.isalnum():
        return False
    
    return True

password = ""

while len(password) < 8:
    caracter = input("Introduce un carácter para el password: ")
    password += caracter

    if validar_password(password):
        print("Password completo:", password)
        break
    else:
        print("El password debe contener al menos 8 caracteres y solo números y letras.")
