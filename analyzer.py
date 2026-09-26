def analyze(old_files, new_files):

    # Counting how many files were changed
    changed = 0

    # Counting how many new files were created
    new_files_count = 0

    # Checking each file from the second scan
    for file in new_files:

        # Checking if the file is newly created
        if file not in old_files:
            new_files_count = new_files_count + 1

        # Check if the file was changed
        elif new_files[file] != old_files[file]:
            changed = changed + 1

    # Starting the risk score from 0
    risk = 0

    # If 5 or more files changed, increase risk by 2
    if changed >= 5:
        risk = risk + 2

    # If at least 1 new file was created, increase risk by 1
    if new_files_count >= 1:
        risk = risk + 1

    # Deciding the final result based on the risk score
    if risk >= 2:
        result = "HIGH RISK"

    elif risk == 1:
        result = "SUSPICIOUS"

    else:
        result = "SAFE"

    # Returning all the results to the main program
    return changed, new_files_count, risk, result