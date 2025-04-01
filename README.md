# unixPasscrack

# Uses the crypt() algorithm which hashes UNIX Passwords

we will create two functions-main and testpass 
it proves a good programming practice to separate your program into separate functions,
each with a specific purpose, allows us to reuse code and makes
the program easier to read.
# main function opens the encrypted password file “passwords.txt” and
 reads the contents of each line in the password file. 
For each line, it splits out the username and the hashed password. 
For each individual hashed password, the main function calls the testPass() function that
tests passwords against a dictionary file.

#  it opens the dictionary and iterates through each word in the dictionary, creating an encrypted
password hash from the dictionary word and the salt. If the result matches
our encrypted password hash, the function prints a message indicating the
found password and returns. Otherwise, it continues to test every word in
the dictionary.
