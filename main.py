from stats import get_num_words, get_num_chars, sort_count_dictionary
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = get_num_words(text) 
	chars = get_num_chars(text)
	sorted_chars = sort_count_dictionary(chars)
	print_report(book_path, num_words, sorted_chars)

def print_report(book_path, num_words, sorted_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for item in sorted_chars:
		print(f"{item[0]}: {item[1]}")

	print("============= END ===============")

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()


main()
