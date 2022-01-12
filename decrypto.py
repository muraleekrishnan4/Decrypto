import argparse
import base64



class Decrypto:

	base64_decoded = ""
	hex_decoded = ""

	###Methods###

	def __init__(self, cipher, mode):
		self.cipher = cipher
		self.mode = mode

	def attack(self):

		if self.mode.lower() == 'magic':
			self.base64()
			self.hex()

			self.printall()


		elif self.mode.lower() == 'base64':
			self.base64()

		elif self.mode.lower() == 'hex':
			self.hex()

		else:
			print("\nInvalid Argument")


	#Hex
	def hex(self):
		print("\n***Hexcode***")
		print("Decoding...")
		try:
			hex_bytes = bytes.fromhex(self.cipher)
			self.hex_decoded = hex_bytes.decode('ascii')
			print("Decoded...")
			print("Decoded Message: ",self.hex_decoded)
		except:
			print("Unable to decode")



	#Base64
	def base64(self):
		print("\n***Base64***")
		print("Decoding...")
		try:
			base64_bytes = self.cipher.encode('ascii')
			decoded_bytes = base64.b64decode(base64_bytes)
			self.base64_decoded = decoded_bytes.decode('ascii')
			print("Decoded...")
			print("Decoded Message: ",self.base64_decoded)
		except:
			print("Unable to decode")


	#Magic
	def magic(self):
		print("\nStarting Magic mode...")
		print("This is try out all possible methods to decrypt. Please wait...")

		#starting attack
		self.base64()




	#Print all decoded
	def printall(self):
		print("\nDecoded Strings","\n***************")

		if self.base64_decoded != "":
			print("Base64 - ",self.base64_decoded) #Base64
		
		if self.hex_decoded != "":
			print("Hex - ", self.hex_decoded) #Hexcode








if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Decode the Crypto')
	parser.add_argument(dest='cipher', help='Enter Cipher Text')
	parser.add_argument('-m', '--mode',default='magic' ,dest='mode', help='Choose the decode mode [default = magic]')
	parser.add_argument('-v', '--version', action = 'version', version='Decrypto v1.0')
	
	args = parser.parse_args()

	cipher = args.cipher
	mode = args.mode

	#Welcome Message
	print("\nLet's turn on Decrypto")


	#Creating object
	dc = Decrypto(cipher, mode)
	dc.attack()
