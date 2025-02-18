import hashlib
from binascii import hexlify

def bytes_to_hex(b):
    return hexlify(b).decode('utf-8')

def string_to_sha1(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    return bytes_to_hex(sha1.digest())

def save_password(password):
    hashed_password = string_to_sha1(password)
    with open("password.txt", "w") as file:
        file.write(hashed_password)

def dictionary_attack():
    # Load the hashed password from the file
    with open("password.txt", "r") as file:
        hashed_password = file.read().strip()

    # Attempt to crack the password
    with open("english.0", "r") as dictionary_file:
        for line in dictionary_file:
            line = line.strip()
            if hashed_password == string_to_sha1(line):
                with open("crackedpassword.txt", "w") as output_file:
                    output_file.write(f"The password is: {line}")
                print(f"Password cracked: {line}")
                return
    print("Password could not be cracked.")
    with open("crackedpassword.txt", "w") as output_file:
        output_file.write("Password could not be cracked.")

def main():
    password = input("Enter your password: ")
    save_password(password)
    dictionary_attack()

if __name__ == "__main__":
    main()
