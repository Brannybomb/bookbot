def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()

	words = file_contents.split()
	word_count = len(words)

	string_int = {}
	for i in file_contents:
		char = i.lower()
		string_int[char] = string_int.get(char, 0) + 1

	# Convert dictionary to a list of tuples
	char_list = [(char, count) for char, count in string_int.items()]

	# Sort the list based on the count in descending order
	char_list.sort(key=lambda item: item[1], reverse=True)

	#Begin report
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word_count} words found in the document")

	# Now char_list is sorted by count
	for char, count in char_list:
    		if char.isalpha():  # Only print alphabetic characters
        		print(f"The '{char}' character was found {count} times")

	#End report
	print("--- End report  ---")
if __name__ == "__main__":
	main()
