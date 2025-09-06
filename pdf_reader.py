#Import libraries
from pypdf import PdfReader
from collections import Counter
import re

#Load PDF
reader = PdfReader("timetable.pdf")

#1.Page count
print("PDF Analysis Report")
print()
print(f"Total pages: {len(reader.pages)}")

#2.Metadata
print("\nPDF Metadata")
meta = reader.metadata
for key, value in meta.items():
    print(f"{key}: {value}")

#3.Search for a keyword
keyword = "CS F111"
found_pages = []
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    if keyword in text:
        found_pages.append(i)

if found_pages:
    print(f"\nKeyword '{keyword}' found on page(s): {found_pages}")
else:
    print(f"\nKeyword '{keyword}' not found in the PDF.")

#4.Extract all text
all_text = "".join(page.extract_text() or "" for page in reader.pages)

#5.Text statistics
print("\nDocument Statistics")
print(f"Total characters: {len(all_text)}")
print(f"Total words: {len(all_text.split())}")
print(f"Total lines: {len(all_text.splitlines())}")

#6.Character frequency
char_freq = {}

for ch in all_text:
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1

#Sorted by frequency
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

print("\nMost Common Characters")
for ch, freq in list(char_freq.items())[:3]:   #Shows top 3
    print(f"{repr(ch)}: {freq}")


#7.Instructor frequency
names = ["Rohit Gupta", "Kurra Suresh", "Aruna Malapati"]  # add more if needed
print("\nInstructor Mentions")
for name in names:
    print(f"{name}: {all_text.count(name)}")

print("\nAnalysis complete")
