def show_alert(changed, new_files, risk, result):

    # Displaying scan result heading
    print("\n==============================")
    print("       SCAN RESULT")
    print("==============================")

    # Displaying the scan information
    print("Changed files :", changed)
    print("New files     :", new_files)
    print("Risk score    :", risk)
    print("Risk level    :", result)

    # Displaying warning for high risk
    if result == "HIGH RISK":

        print("\nWARNING!")
        print("Suspicious file activity detected.")

    # Displaying warning for suspicious activity
    elif result == "SUSPICIOUS":

        print("\nCAUTION!")
        print("Some unusual activity was detected.")

    # Displaying message when no suspicious activity is found
    else:

        print("\nFolder appears normal.")