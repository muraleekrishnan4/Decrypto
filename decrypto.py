import base64



class Decrypto:

	base64_decoded = ""

	###Methods###

	#Base64
	def base64(self, cipher):
		print("\n***Base64***")
		print("Decoding...")
		try:
			base64_bytes = cipher.encode('ascii')
			decoded_bytes = base64.b64decode(base64_bytes)
			self.base64_decoded = decoded_bytes.decode('ascii')
			print("Decoded")
		except:
			print("Unable to decode")


	#Magic
	def magic(self, cipher):
		print("\nStarting Magic mode...")
		print("This is try out all possible methods to decrypt. Please wait...")

		#starting attack
		self.base64(cipher)

	#Printing the decoded string
	def print(self, option):
		print("\n*****************\nDecoded Messages \n*****************")

		if option == 1: #Magic
			print("Base64 - ",self.base64_decoded)
		elif option == 2: #Base64
			print("Base64 - ",self.base64_decoded)


		print("\n")




###Functions###

#Prints Menu
def menu():
	print("""1. Magic mode (Attempts all methods) 
2. Base64""")
	return int(input("Choose an option: "))



#Welcome Message
print("Welcome to Decrypto")

cipher = input("Enter the string: ")

#Prints Main menu and returns user option
option = menu()

#Creating object
dc = Decrypto()


if option == 1:
	dc.magic(cipher)
elif option == 2:
	dc.base64(cipher)
else:
	print("Invalid option!!!")


#Prints Decoded Message
dc.print(option)