st = "dheeraj"
def count(string):
	st = st.lower()
	if len(st) <= 0:
		return 0
	elif st[0] in ("a", "e", "i", "o", "u"):
            return 1 + count(st[1:])
        else:
            return count(st[1:])
	
