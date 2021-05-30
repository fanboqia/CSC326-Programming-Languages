def split_sentence(fileName):
	'''split sentence'''
	# read the file into a string
	f = open(fileName,'r')
	txt = f.read()

	# process the string according to the five rules
	# (. he) Periods followed by whitespace followed by a lower case letter are not sentence boundaries. 
	# (.9) Periods followed by a digit with no intervening whitespace are not sentence boundaries. 
	# (Mr. Smith) Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
	# (e.g) Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
	# (true...) Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

	name_title = ['Mr','Mrs','Jr','Dr']
	txt = list(txt)
	length = len(txt)
	for i in range(length):
		if (txt[i] == '.' or txt[i] == '!' or txt[i] == '?') and i != length - 1 and i != 0:
			if txt[i+1] == ' ' and txt[i+2].islower():
				continue
			if txt[i+1].isdigit():
				continue
			if txt[i-1].isalpha() and txt[i+1].isalpha():
				continue
			if txt[i+1] == '.' or txt[i+1] == ',':
				continue
			if txt[i-1] == 'r' and txt[i-2] == 'M':
				continue
			if txt[i-1] == 's' and txt[i-2] == 'r' and txt[i-3] == 'M':
				continue
			if txt[i-1] == 'r' and txt[i-2] == 'J':
				continue
			if txt[i-1] == 'r' and txt[i-2] == 'D':
				continue

			txt[i+1] = '\n'
	txt = ''.join(txt)
	return txt
# hard code
print split_sentence('q5File.txt')
