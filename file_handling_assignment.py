try:
    with open('my_file.txt', 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 42\n")

        print("File 'my_file.txt' created and initial content written.")

    with open('my_file.txt', 'r') as file:
        print("\nContents of 'my_file.txt':")
        for line in file:
            print(line.strip())

    with open('my_file.txt', 'a') as file:

        file.write("\nAppending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")

        print("\nAdditional lines appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("\nFile handling process complete.")

