def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "__CONTENT_START__\n" \
               "__NO_SUCH_FILE__\n" \
               "__CONTENT_END__"
    else:
        return f"__CONTENT_START__\n" \
               f"{content}" \
               f"__CONTENT_END__"
    finally:
        print(f"Attempted to read file: {file_name}")


print(read_file("one_lined_file.txt"))
print()
print(read_file("file_does_not_exist.txt"))
