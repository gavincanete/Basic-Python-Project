# Basic-Python-Project
List of Simple Applications using Python

<strong>Programs Prerequisite</strong><br>
Add this following command:
```
pip install pyfiglet (For Hangman)
pip install pyperclip (For Password Gen)
```
<strong>Running the Hangman Game</strong>
```
cd Hangman/
python hangman.py
```
<i>Note: should include the candidate_words.txt upon running the app</i>

<strong>Running the Cipher App</strong>
```
cd EncryptionProgram/
python cipher_app.py
```

<strong>Running the Password Generator</strong>
```
cd PasswordGenerator/
python password_generator_app.py
```
<strong>Prerequisite for Addressbook</strong>
```
SQL Knowledge for setting up
(1) Must have Mysql
(2) Required Table:
|__Fields____ |_____Type___ |
|ID           |int          |
|firstName    |varchar(255) |
|middleInitial|varchar(2)   |
|lastName     |varchar(255) |
|address      |varchar(255) |

(3) Change the credential under 
./AddressBook/address_book_db.py 
locate Class AddressBookDB()
locate __init__ function
change the root password (****) to your appropriate password
```
<strong>Running the Addressbook</strong>
```
cd AddressBook/
python address_book_app.py
```
