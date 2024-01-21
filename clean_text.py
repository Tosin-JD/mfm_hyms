import os

directory = ""

# Create a directory for cleaned files if it doesn't exist
cleaned_directory = os.path.join(directory, "cleaned")
if not os.path.exists(cleaned_directory):
    os.makedirs(cleaned_directory)

# Loop through all files from 1.txt to 1504.txt
for file_number in range(1, 1505):
    file_name = os.path.join(directory, f"{file_number}.txt")
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Initialize an empty list to store the cleaned lines
    cleaned_lines = []
    print(lines)

    # Process each line
    for line in lines:
        line = line.strip()

        # Check if the line starts with a dash
        if line.startswith("-"):
            # If the line starts with a dash, add two newline characters
            cleaned_lines.append("\n" + line)
        else:
            # If the line doesn't start with a dash, keep it as it is
            cleaned_lines.append(line)

    # Write the cleaned lines to a new file in the "cleaned" directory
    cleaned_file_name = os.path.join(cleaned_directory, f"{file_number}.txt")
    with open(cleaned_file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(cleaned_lines))
    print(f"File {file_number}.txt cleaned and saved in the 'cleaned' folder")
    print()
