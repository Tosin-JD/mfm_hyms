# Read the contents of the file
with open('495.txt', 'r') as file:
    text = file.read()

# Iterate through each character in the text
for i, char in enumerate(text):
    if char == '\n':
        print(f"Line Feed (\\n) found at position {i}")
    elif char == '\r':
        print(f"Carriage Return (\\r) found at position {i}")
    else:
        print(char, end='')  # Print the character without newline

# Optional: Print a summary of total counts
count_n = text.count('\n')
count_r = text.count('\r')
print(f"\nTotal Line Feeds (\\n): {count_n}")
print(f"Total Carriage Returns (\\r): {count_r}")