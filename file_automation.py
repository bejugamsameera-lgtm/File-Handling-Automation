# file_automation.py
# file_automation.py
# --------------------------------------------
# Python File Handling,automation logic and exception handling
# Demonstrates:
# 1. Reading and writing text files
# 2. Reading and writing CSV files
# 3. Renaming files
# 4. Moving files to another folder
# 5. Deleting files
# 6. Exception handling using try-except
# --------------------------------------------

import os
import csv
import shutil

print("--- Python File Handling and Automation logic and execption handling ---")

# -------------------------------------------------
# 1. Create and write to a text file
# -------------------------------------------------
try:
    print("\n1. Creating and writing to sample.txt...")

    # Open the file in write mode. If the file does not exist,
    # Python will create it automatically.
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a sample text file.\n")
        file.write("This file is used to demonstrate Python file handling.\n")

    print("sample.txt created successfully.")

except Exception as e:
    print("Error while creating sample.txt:", e)


# -------------------------------------------------
# 2. Read the text file
# -------------------------------------------------
try:
    print("\n2. Reading from sample.txt...")

    with open("sample.txt", "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except FileNotFoundError:
    print("sample.txt was not found.")
except Exception as e:
    print("Error while reading sample.txt:", e)


# -------------------------------------------------
# 3. Create and write to a CSV file
# -------------------------------------------------
try:
    print("\n3. Creating and writing to data.csv...")

    # Data to write into the CSV file
    rows = [
        ["ID", "Name", "Course"],
        [1, "Sameera", "Python"],
        [2, "Haritha", "Machine Learning"],
        [3, "Anitha", "Web Development"]
    ]

    # newline='' prevents extra blank lines in CSV on Windows
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("data.csv created successfully.")

except Exception as e:
    print("Error while creating data.csv:", e)


# -------------------------------------------------
# 4. Read the CSV file
# -------------------------------------------------
try:
    print("\n4. Reading from data.csv...")

    with open("data.csv", "r") as file:
        reader = csv.reader(file)

        print("CSV Data:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("data.csv was not found.")
except Exception as e:
    print("Error while reading data.csv:", e)


# -------------------------------------------------
# 5. Rename sample.txt to notes.txt
# -------------------------------------------------
try:
    print("\n5. Renaming sample.txt to notes.txt...")

    os.rename("sample.txt", "notes.txt")

    print("File renamed successfully.")

except FileNotFoundError:
    print("sample.txt does not exist.")
except Exception as e:
    print("Error while renaming file:", e)


# -------------------------------------------------
# 6. Move notes.txt to backup folder
# -------------------------------------------------
try:
    print("\n6. Moving notes.txt to backup/ folder...")

    # Create the folder if it does not already exist
    os.makedirs("backup", exist_ok=True)

    # Move the file into the backup folder
    shutil.move("notes.txt", "backup/notes.txt")

    print("File moved successfully.")

except FileNotFoundError:
    print("notes.txt does not exist.")
except Exception as e:
    print("Error while moving file:", e)


# -------------------------------------------------
# 7. Delete data.csv
# -------------------------------------------------
try:
    print("\n7. Deleting data.csv...")

    os.remove("data.csv")

    print("data.csv deleted successfully.")

except FileNotFoundError:
    print("data.csv does not exist.")
except Exception as e:
    print("Error while deleting data.csv:", e)


# -------------------------------------------------
# Program Completed
# -------------------------------------------------
print("\n--- Program completed successfully! ---")
