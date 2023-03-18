import re


# Reads a file in blocks of a specified size and yields each block as it's read.
def read_file_in_blocks(filename, size=2048):
    with open(filename, 'rb') as f:
        while 1:
            block = f.read(size)
            if not block:
                break
            yield block


# Displays the secret messages found in the image file.
def display():
    for message in secret_message_iterator:
        print(message.decode('ascii'))


# Finds all secret messages in the image file 'logo.jpg' that match the specified pattern and yields them one by one.
secret_message_iterator = (
    message for block in read_file_in_blocks('logo.jpg')
    for message in re.findall(rb'\b[a-z]{5,}!\b', block)
)

display()
