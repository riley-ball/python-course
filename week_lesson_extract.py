import re

# Read the output.txt file
with open('output.txt', 'r') as file:
    content = file.read()

# Use regular expressions to extract week number, title, and lesson
pattern = r"Week (\d+): (.+)\n\nLesson: (.+)"
matches = re.findall(pattern, content, re.MULTILINE)

# Create a list of dictionaries to store the week information
weeks = []
for match in matches:
    week_number = match[0]
    week_title = match[1]
    week_lesson = match[2]

    week_info = {
        'week_number': week_number,
        'week_title': week_title,
        'week_lesson': week_lesson
    }
    weeks.append(week_info)

# Print the extracted information
for week in weeks:
    print(f"Week {week_info['week_number']}: {week_info['week_title']}\n\nLesson: {week_info['week_lesson']}\n\n")
    print()
