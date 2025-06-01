
import re
from collections import Counter

def parse_chat(file_path):
    pattern = re.compile(r"(.*?)[\s\-–]+(.*?):\s+(.*)")
    messages = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                match = pattern.match(line)
                if match:
                    timestamp, sender, message = match.groups()
                    messages.append((sender.strip(), message.strip(), timestamp.strip()))
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    return messages

def analyze_chat(messages):
    sender_counter = Counter()
    word_counter = Counter()

    for sender, message, timestamp in messages:
        sender_counter[sender] += 1
        words = message.lower().split()
        word_counter.update(words)

    print("\n📊 Top Senders:")
    for sender, count in sender_counter.most_common():
        print(f"{sender}: {count} messages")

    print("\n📝 Most Used Words:")
    for word, count in word_counter.most_common(10):
        print(f"{word}: {count} times")

def main():
    print("📂 WhatsApp Chat Analyzer (Universal Format)")
    file_path = "Chat.txt"
    messages = parse_chat(file_path)
    if messages:
        analyze_chat(messages)
    else:
        print("⚠️ No messages parsed. Check if Chat.txt has correct content.")

if __name__ == "__main__":
    main()
