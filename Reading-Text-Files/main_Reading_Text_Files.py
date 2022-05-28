def read_file_content(filename):
	read_file_content = (open("story.txt", "r")).read()
	return read_file_content

read_file_content("./story.txt")

def count_words():
	text = read_file_content("./story.txt")
	text= text.lower()
	text=text.replace("?", "")
	text=text.replace(".", "")
	text=text.replace("'", "")
	text=text.replace(",", "")
	text=text.replace("!", "")
	text=text.replace(":", "")
	split_text = text.split()
	counts = dict() 
	for word in split_text:
		if word in counts:
			counts[word] = +1
		else:
			counts[word] = 1
	return(counts)
print(count_words())	

    # return {"as": 10, "would": 20}
