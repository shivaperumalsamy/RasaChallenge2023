def write_content_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to '{filename}'.")
    except IOError:
        print(f"Error writing to '{filename}'.")