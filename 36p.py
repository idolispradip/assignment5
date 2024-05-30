def count_whitespaces(file_path):
    try:
        num_whitespaces = 0

        with open(file_path, 'r') as file:
            for line in file:
                num_whitespaces += line.count(' ')
                num_whitespaces += line.count('\t')

        print(f"Number of whitespaces: {num_whitespaces}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An IOError occurred while trying to read the file '{file_path}'.")

file_path = 'example.txt'
count_whitespaces(file_path)
