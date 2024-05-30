def count_text_properties(file_path):
    vowels = 'aeiouAEIOU'
    num_chars = 0
    num_vowels = 0
    num_consonants = 0
    num_words = 0
    num_lines = 0

    with open(file_path, 'r') as file:
        for line in file:
            num_lines += 1
            num_chars += len(line)
            num_words += len(line.split())

            for char in line:
                if char.isalpha():
                    if char in vowels:
                        num_vowels += 1
                    else:
                        num_consonants += 1

    print(f"Number of characters: {num_chars}")
    print(f"Number of vowels: {num_vowels}")
    print(f"Number of consonants: {num_consonants}")
    print(f"Number of words: {num_words}")
    print(f"Number of lines: {num_lines}")

file_path = 'example.txt'
count_text_properties(file_path)
