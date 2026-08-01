1.	Write program demonstrates how to use regular expressions in Python to match and search for patterns in text.

import re
text = "My email is student123@gmail.com and my phone number is 9876543210."
pattern_match = r"My"
match = re.match(pattern_match, text)
if match:
    print("Match found at the beginning:", match.group())
else:
    print("No match found at the beginning.")
pattern_search = r"\d{10}"   # Pattern for a 10-digit phone number
search = re.search(pattern_search, text)
if search:
    print("Phone number found:", search.group())
else:
    print("Phone number not found.")
email_pattern = r"\S+@\S+\.\S+"
email = re.search(email_pattern, text)
if email:
    print("Email found:", email.group())
else:
    print("Email not found.")
