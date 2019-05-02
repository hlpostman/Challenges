# knuth_morris_pratt.py
# May 2019

def knuth_morris_pratt_algorithm(string: str, substring: str) -> bool:
	# Build helper table
	substring_internal_matches = [-1 for _ in substring]
	i, j = 1, 0
	while i < len(substring):
		if substring[i] == substring[j]:
			substring_internal_matches[i] = j
			i += 1
			j += 1
			continue
		j = substring_internal_matches[j - 1] + 1 
		if substring[i] == substring[j]:
			continue
		else:
			i += 1
	# Search in big string for substring
	i, j = 0, 0
	while i < len(string):
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
			continue
		j = substring_internal_matches[j - 1] + 1
		if string[i] == substring[j]:
			continue
		else:
			i += 1
			j = 0
	return False
	
def longest_repeated_prefix(s: str) -> str:
	substring_internal_matches = [-1 for _ in s]
	i, j = 1, 0
	while i < len(s):
		if s[i] == s[j]:
			substring_internal_matches[i] = j
			i += 1
			j += 1
			continue
		j = substring_internal_matches[j - 1] + 1 
		if s[i] == s[j]:
			continue
		else:
			i += 1
	start, end = 0, max(substring_internal_matches) + 1
	return s[start:end]
