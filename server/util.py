def write_content_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write("\n"+content)
        print(f"Content successfully written to '{filename}'.")
    except IOError:
        print(f"Error writing to '{filename}'.")