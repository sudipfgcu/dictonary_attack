import hashlib
from binascii import hexlify
import time

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

    attempts = 0
    start_time = time.time()
    
    # Attempt to crack the password
    with open("english.0", "r") as dictionary_file:
        for line in dictionary_file:
            line = line.strip()
            attempts += 1
            if hashed_password == string_to_sha1(line):
                elapsed_time = time.time() - start_time
                with open("crackedpassword.txt", "w") as output_file:
                    output_file.write(f"The password is: {line}\n")
                    output_file.write(f"Attempts: {attempts}\n")
                    output_file.write(f"Time taken: {elapsed_time:.2f} seconds\n")
                print(f"Password cracked: {line}")
                print(f"Attempts: {attempts}")
                print(f"Time taken: {elapsed_time:.2f} seconds")
                return

    elapsed_time = time.time() - start_time
    print("Password could not be cracked.")
    print(f"Attempts: {attempts}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    with open("crackedpassword.txt", "w") as output_file:
        output_file.write("Password could not be cracked.\n")
        output_file.write(f"Attempts: {attempts}\n")
        output_file.write(f"Time taken: {elapsed_time:.2f} seconds\n")

def main():
    password = input("Enter your password: ")
    save_password(password)
    dictionary_attack()

if __name__ == "__main__":
    main()
