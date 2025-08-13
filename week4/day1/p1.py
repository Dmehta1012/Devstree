
# with open("prac1.txt", "w") as f:
#     content = (
#         "Python is a popular programming language known for \n"
#         "its simplicity and versatility. It is widely used in web development, \n"
#         "data analysis, artificial intelligence, and automation. \n"
#         "Many developers prefer Python because of its easy-to-read syntax and large community support."
#     )
#     f.write(content)
#     print("File created successfully!")

with open(r"C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day1\prac1.txt", "r") as f:
    data = f.read()


line_count = len(data.splitlines())     
char_count = len(data)                  
word_count = len(data.split())          


print("\nThis is for Word Counter")
n = input("Enter any word to find in this paragraph: ")
print(f"'{n}' appears {data.count(n)} times in the paragraph.")


print("\n____ Finding how many Characters in paragraph ____")
print(f"Number of Characters in the paragraph: {char_count}")

print("\n____ How many lines ____")
print(f"Number of lines: {line_count}")

print("\n____ How many words ____")
print(f"Number of words: {word_count}")


with open(r"C:\Users\devarsh mehta\OneDrive\AppData\Desktop\Devstree\week4\day1\results.txt", "w") as result:
    result.write(f"Lines: {line_count}\n")
    result.write(f"Words: {word_count}\n")
    result.write(f"Characters: {char_count}\n")
    result.write(f"'{n}' count: {data.count(n)}\n")

print("\nResults saved to results.txt") 
