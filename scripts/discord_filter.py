import re
import os

def extract_messages(input_file, output_file, sender):
    omit_keywords = {
        "Attachments",
        "Reactions",
        "Embed",
        "tenor",
        "https"
    }

    # Pattern for Discord timestamps like: [8/1/2024 9:12 PM] exbo888
    message_pattern = re.compile(r'^\[\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}\s*[APMapm]{2}\] ')

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        lines = infile.readlines()

    messages = []
    current_message = ""

    for line in lines:
        if message_pattern.match(line):
            if current_message:
                messages.append(current_message.strip())
            current_message = line
        else:
            current_message += line
    if current_message:
        messages.append(current_message.strip())

    filtered_messages = []
    for msg in messages:
        if f"] {sender}" in msg and not any(keyword in msg for keyword in omit_keywords):
            message_text = msg.split(f"] {sender}", 1)[1].strip()
            filtered_messages.append(message_text)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for message in filtered_messages:
            outfile.write(message + '\n')


if __name__ == '__main__':
    subject = 'exbo888'
    root = 'messages/discord'
    output_dir = 'messages/output'
    os.makedirs(output_dir, exist_ok=True)

    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.txt'):
                input_file = os.path.join(dirpath, filename)
                output_file = os.path.join(
                    output_dir,
                    f"{os.path.splitext(filename)[0]}_{subject}.txt"
                )
                print(f"Processing {input_file} → {output_file}")
                extract_messages(input_file, output_file, subject)