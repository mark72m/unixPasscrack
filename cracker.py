#######################################################################################
#                                UNIX Password Cracker                                #
#                 Uses the crypt() Algorithm which hashes UNIX Passwords              #
#  Opens a dictionary and iterates through each word creates an encrypted pass Hash   #
#  from the word and the salt. If result matches our encrypted pass hash, it prints   #
#  password found otherwise, it continues to test every word in the dictionary...     #
#######################################################################################

import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt', 'r')

	for wordd in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)

		if (cryptWord == cryptPass):
			print ("[+] Password Found: " + word + "\n")
			return

	print ("[-] Password Not Found. \n")
	return

def main():
	passFile = open('password.txt')

	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print ("[+] Cracking Password for: " + user)
			testPass(cryptPass)

if __name__ == "__main__":
	main()
