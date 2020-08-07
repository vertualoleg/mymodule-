def split(string,chars):
    output = []
    string_split=''
    for char_string in string:
        string_bool = True
        for char in chars:
            if char_string == char:
                output.append(string_split)
                string_split=''
                string_bool = False
        if string_bool:
            string_split += char_string
    output.append(string_split)
    return output
