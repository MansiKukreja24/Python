def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

string: str=input()
print(paper_doll(string))
