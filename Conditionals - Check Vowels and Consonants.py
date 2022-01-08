st = "Score: 36"
if not st:
	print("Empty String")
else:
	for char in st.lower():
		if char in ("a", "e", "i", "o", "u"):
			print(f"{char} is a vowel")
		elif not char.isalpha():
			print(f"{char} is not a letter")
		else:
			print(f"{char} is a consonant")


    
