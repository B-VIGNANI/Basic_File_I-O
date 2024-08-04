def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {filename}")
    except IOError as e:
        print(f"An error occurred : {e}")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except IOError as e:
        print(f"An error occurred : {e}")
        return None

def main():
    filename = "content.txt"
    inputs = input("Please enter a string to write to the file: ")
    write_to_file(filename,inputs)
    content = read_from_file(filename)
    if content is not None:
        print("\nContent of the file:")
        print(content)

if __name__ == "__main__":
    main()
