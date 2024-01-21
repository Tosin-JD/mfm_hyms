import os

directory = ""

cleaned_directory = os.path.join(directory, "cleaned")
if not os.path.exists(cleaned_directory):
    os.makedirs(cleaned_directory)

for file_number in range(1, 1505):
    file_name = os.path.join(directory, f"{file_number}.txt")
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []
    previous_line = ""

    for line in lines:
        line = line.strip()
        if len(line) < 15 and previous_line.endswith(('!', ',', '.')):
            previous_line += " " + line
        else:
            if previous_line:
                cleaned_lines.append(previous_line)
            previous_line = line

    # Add the last line if it was not merged
    if previous_line:
        cleaned_lines.append(previous_line)

    # Replacing triple newline characters with two newline characters
    cleaned_text = "\n".join(cleaned_lines)
    cleaned_text = cleaned_text.replace("\n\n\n", "\n\n")

    cleaned_file_name = os.path.join(cleaned_directory, f"{file_number}.txt")
    with open(cleaned_file_name, "w", encoding="utf-8") as file:
        file.write(cleaned_text)
    print(f"File {file_number}.txt cleaned and saved in the 'cleaned' folder")
