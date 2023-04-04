with open('cPos.txt', 'r') as f:
    lines = f.readlines()

cleaned_lines = []
for i, line in enumerate(lines):
    if line.strip() == '' and i > 0 and lines[i-1].strip() != '':
        # If the current line is blank and the previous line is not blank
        # and this is not the first line, skip the line
        continue
    cleaned_lines.append(line)

with open('cPositive.txt', 'w') as f:
    f.writelines(cleaned_lines)