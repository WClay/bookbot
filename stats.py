def get_num_words(text):
	words = text.split()
	return len(words) 

def get_num_chars(text):
	characters = {}
	text = text.lower()
	for char in list(text):
		if char in characters:
			characters[char] += 1
		else: characters[char] = 1
		
	return characters

def sort_count_dictionary(dictionary):
	return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)