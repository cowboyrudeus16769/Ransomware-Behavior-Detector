import os

# Geting information about all files in the given folder
def get_files(folder):

    # Create an empty dictionary to store file information
    files = {}

    # Going through each item in the folder
    for file in os.listdir(folder):

        # Create the complete path of the file
        path = os.path.join(folder, file)

        # Check if the item is a file
        if os.path.isfile(path):

            # Store the file name and its last modified time
            files[file] = os.path.getmtime(path)

    # Return the list of files and their modified times
    return files