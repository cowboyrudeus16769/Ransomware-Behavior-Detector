import time
import monitor
import analyzer
import alert
import logger

# Display program title
print("================================")
print("   RANSOMWARE BEHAVIOR DETECTOR")
print("================================")

while True:

    # Show options to the user
    print("\n1. Scan a folder")
    print("2. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Scaning a folder for ransomware behavior
    if choice == "1":

        # Asking the user for folder location by folder path
        folder = input("Enter folder path: ")

        try:
            # First scan of the folder for files
            print("\nTaking first scan...")
            old_files = monitor.get_files(folder)

            print("Files found:", len(old_files))

            # Waiting for 30 seconds for the user to add/remove files in the folder
            print("Monitoring for 30 seconds...")
            time.sleep(30)

            # Scan the folder again for files
            print("\nTaking second scan...")
            new_files = monitor.get_files(folder)

            # Comparing the two scans for changes in the folder and analyzing the risk of ransomware behavior
            changed, new_files_count, risk, result = analyzer.analyze(old_files, new_files)

            # Showing the result
            alert.show_alert(changed, new_files_count, risk, result)

            # Saving result in log file
            logger.save_log(result)

            print("\nResult saved in log.txt")

        # If folder path is wrong then show error message
        except:
            print("\nFolder not found!")
            print("Please check the folder path.")

    # Option 2: Exit program if user enters 2
    elif choice == "2":
        print("\nProgram closed.")
        break

    # If user enters anything else print invalid choice message
    else:
        print("\nInvalid choice!")