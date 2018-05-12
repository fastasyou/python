import string
alphabet = " " + string.ascii_lowercase
print(alphabet)

def encoding(message, key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string

message = "hi my name is caesar"
encoded_message = encoding(message, 3)
print(encoded_message)