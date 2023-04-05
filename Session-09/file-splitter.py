def read_text_file(filename):
    f_handle = open(filename, "r")
    content = f_handle.readlines()
    return content


def extract_isbn(text):
    result = ""
    for index in range(1, len(text)):
        if text[index].isupper():
            result = text[:index]
            break
    return result


def extract_author(text):
    result = ""
    for index in range(1, len(text)):
        if text[index] == '"':
            result = text[:index]
            break
    return result


def remove_characters(text="abcde ", find_this=[], replace_with=""):
    result = text
    for characters in find_this:
        result = result.replace(characters, replace_with)
    return result


def main():
    list_of_lines = read_text_file("data.txt")
    for line in list_of_lines:
        isbn = extract_isbn(line)
        remaining_text = line[len(isbn)::]
        author = extract_author(remaining_text)
        title = remaining_text[len(author)::]
        author = remove_characters(author, ["+"], " ")
        title = remove_characters(title, ['"'], "")
        print(f"|{isbn}|{author}|{title}")


if __name__ == '__main__':
    main()
