# By using readline one line will return
with open("text.txt", "r") as file:
    f = file.readline()
    s = file.readline()
print("First line:", f)
print("Second line:", s)

# readlines will read all line from file and return list of string
with open("text.txt", "r") as file:
    all_lines = file.readlines()
print(all_lines)

# Writelines used to write a list of strings to a file
lines = ["Hello Python!", "\nLearning File Handling", "\nUse writelines"]

with open("text.txt", "w") as file:
    file.writelines(lines)

with open("text.txt", "r") as file:
    f = file.read
print(file.read)

# remove one line from file
# Read the file and store its content in a list
with open("text.txt", "r") as file:
    lines = file.readlines()

# Remove the specific line (e.g., remove the second line)
line_to_remove = 1  # index of the line to remove (0-based index)
if 0 <= line_to_remove < len(lines):
    lines.pop(line_to_remove)

# Write the modified content back to the file
with open("text.txt", "w") as file:
    file.writelines(lines)

