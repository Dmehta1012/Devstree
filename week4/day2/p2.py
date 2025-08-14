def read_file(filename):
    try:
        with open(filename,"r") as f:
            content=f.read()
        print(f"content of '{filename}':\n {content}")  
    except FileNotFoundError:
        print(f"file {filename} is doesn't Exits")
    except PermissionError:
        print(f"you don't have to access to open the file {filename}")
    except OSError as e:
        print(f"OS error{e}")
    except Exception as e:
        print(e)
def write_file(filename, text):
    
    try:
        with open(filename, "w") as f:
            f.write(text)
        print(f" Written to '{filename}' successfully.")
    except PermissionError:
        print(f" Error: You don't have permission to write to '{filename}'.")
    except OSError as e:
        print(f" OS Error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")

def append_file(filename, text):
    
    try:
        with open(filename, "a") as f:
            f.write(text)
        print(f" Appended to '{filename}' successfully.")
    except PermissionError:
        print(f" Error: You don't have permission to append to '{filename}'.")
    except OSError as e:
        print(f" OS Error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")

def file_op():
    while True:
        print("File Operations Menu")
        print("1.Read File\n")
        print("2.Write File\n")
        print("3.Append file\n")
        print("4.exit\n")

        choice=input("enter choice between (1-4)")
        if choice=='1':
            filename=input("Enter file name to read")
            read_file(filename)
        elif choice=='2':
            filename=input("Enter  file name to write")
            text=input("Enter text to write")
            read_file(filename)
            read_file(text)
        elif choice=='3':
            filename = input("Enter file name to append to: ")
            text = input("Enter text to append: ")
            append_file(filename, text)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Enter valid  umber between (1-4)")
            

file_op()
# write_file("example.txt", "Hello, world!\n")

# append_file("example.txt", "This is an appended line.\n")


# read_file("example.txt")