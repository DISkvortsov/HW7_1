import os

text = []
texts_name = os.listdir("files")

for name in texts_name:
    with open(f"files/{name}", encoding="utf-8") as f:
        lines = f.readlines()
        count_line = str(len(lines))
        lines = [name + "\n"] + [count_line + "\n"] + lines
        text.append(lines)
final_text = "".join(sum((sorted(text, key=len)), []))

with open("final_file.txt", "w", encoding="utf-8") as f:
    f.write(final_text)