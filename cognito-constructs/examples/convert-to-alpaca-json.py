import json
import re

# Path to input text file
import glob

# Path to all input text files
input_files = sorted(glob.glob("example-*.txt"))
output_file = "dataset.json"

def parse_text_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    data = []
    current_prompt = ""
    current_response = []
    parsing_response = False

    for line in lines:
        line = line.strip()

        # Identify prompt
        if line.startswith("1. Prompt:"):
            parsing_response = False  # Reset flag
            current_prompt = ""
            current_response = []
            continue  # Skip header

        # Identify response start
        elif re.match(r"^\d+\. .*", line):
            parsing_response = True
            continue  # Skip line number

        # Collect prompt
        if not parsing_response:
            current_prompt += " " + line if current_prompt else line

        # Collect response
        else:
            current_response.append(line)

    if current_prompt and current_response:
        data.append({
            "instruction": current_prompt.strip(),
            "input": "",
            "output": "\n".join(current_response).strip()
        })

    return data

# Convert text to structured JSON
dataset = []
for file in input_files:
    dataset.extend(parse_text_file(file))

# Save to JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4)

print(f"Dataset saved as {output_file}")
