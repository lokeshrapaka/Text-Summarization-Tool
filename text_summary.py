from transformers import pipeline

# 1. Load the pre-trained summarization model from Hugging Face
summarizer = pipeline("summarization")

# 2. Provide the path to your text file (update this if your file name is different)
file_path = r"article.txt"  # Change 'article.txt' to your actual file name

# 3. Read the content of the text file
try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# 4. Check if text is long enough
if len(text.split()) < 50:
    print("The text is too short to summarize. Please provide a longer article.")
    exit()

# 5. Summarize the text
try:
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    print("\n🔹 Summary:\n")
    print(summary[0]['summary_text'])
except Exception as e:
    print(f"Error during summarization: {e}")
