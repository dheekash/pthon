import string

s = "The quick brown fox jumps over the lazy dog"

set_s = set(s.lower())
set_s.remove(" ")
print(set_s == set(string.ascii_lowercase))
