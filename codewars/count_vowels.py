def get_count(sentence):
	vowels_num = 0
	vowels = ["a", "o", "i", "u", "e"]
	for char in sentence:
		if char in vowels:
			vowels_num += 1
	return vowels_num