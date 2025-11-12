def shutdown():
    """Function to shut down the computer based on user confirmation."""
    choice = input("Do you want to shut down your computer? (yes/no): ").strip().lower()
    
    if choice in ['yes', 'y']:
        print("Shutting down...")
    elif choice in ['no', 'n']:
        print("Shutdown canceled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")