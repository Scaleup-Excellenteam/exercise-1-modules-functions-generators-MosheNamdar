from os import listdir, path

# Define a function to get a valid path from the user
def get_path():
    while 1:
        user_path = input("Please enter a path: ")
        # Check if the entered path exists
        if path.exists(user_path):
            return user_path
        else:
            # If the path is not valid, prompt the user to enter a valid path
            print("The path is not valid, you can try again!")

# Define a function to find files in the given path that start with "deep"
def find_files(user_path):
    files = []
    # Iterate over all files in the given path
    for file in listdir(user_path):
        # Check if the file starts with "deep"
        if file.startswith("deep"):
            # If the file matches the criteria, add its basename to the list of files
            files.append(path.basename(file))
    return files

# Define a function to display the list of files
def display_files(files):
    for file in files:
        # Print each file name on a separate line
        print(file)

# Define the main function to run the program
def main():
    # Prompt the user to enter a valid path
    user_path = get_path()
    # Find files in the given path that start with "deep"
    files = find_files(user_path)
    # Display the list of files
    display_files(files)


if __name__ == "__main__":
    main()

