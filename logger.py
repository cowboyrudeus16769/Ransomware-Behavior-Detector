def save_log(result):

    # Opening the log file in append mode
    file = open("log.txt", "a")

    # Saving the result in the log file
    file.write(result + "\n")

    # Closing the file
    file.close()