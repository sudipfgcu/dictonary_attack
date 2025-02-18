# Dictionary Attack
This repository contains a simple example of a dictionary attack coded in Java.

## Description of Repository Content

Here are the files you can find in this repository:
* `password.txt` is the password typed by user
* `DictionaryAttack.java` is the source code for the attack
* `attack.py` is the python script for the attack
* `english.0` is the dictionary used during the attack to recover passwords
* `crackedpassword.txt` is the password that was gussed right

## Description of the `password.txt` file format

The password user enters from the terminal 


The passwords are hashed using SHA-1 (see attack source code for implementation
in the Java Cryptography Extension). When a salt is used, it is simply concatenated together with the passwords as follows: `salt || password`.

## Description of the attack

The attack simply reads the dictionary line by line and computes 6 different 
possible hashed passwords for the word contained in each line. These 6 possible
hashes are compared to the password contained in the `password.txt` 
file for a match. If there is a match, we recovered a password. If not, we 
simply keep reading the dictionary line by line. 

The 6 possible hashes computed for each `word` from the dictionary are:
* `SHA1(word)`
* `SHA1(drow)` (reversed word)
* `SHA1(wrd)` (word without vowels)
* `SHA1(salt||word)` (salted word)
* `SHA1(salt||drow)` (salted reversed word)
* `SHA1(salt||wrd)` (salted word without vowels)

Note that the salts used in salted hashes are the ones includes in the 
`password.txt` file.

## How to run the attack

To run the attack, simply run attack.py python script
All paths are hardcoded in the file so you will need to update them before 
you compile the source code. 



## Note on complexity

Note that this attack is a simple example and could be made far more efficient
using various strategies. One of them would be to precompute the possible 
hashes before checking the password list for matches. Since our password list
and dictionary are fairly small in this example, I did not implement this 
feature.  

## Task for Students

Add more words to the dictonary by copy pasting passwords list from: https://web.archive.org/web/20120207113205/http://www.insidepro.com/eng/download.shtml
into the english.0 file.
Make your english.0 file as large as possible
