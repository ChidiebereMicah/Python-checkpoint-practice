def RetainFirstHalf(text):
    text_len = len(text)
    half_len = int(text_len/2)
    output = ''
    if text == '':
        return ''
    elif text_len == 1:
        return text
    else:
        for i in range(half_len):
            output = output + text[i]
    return output

def RetainFirstHalfWithSlice(text):
    text_len = len(text)
    half_len = text_len//2
    if text_len == 1:
        return text
    else:
        return text[:half_len]


print(RetainFirstHalf('hippopotamus'))
print(RetainFirstHalf("This is the 1st halfThis is the 2nd half"))
print(RetainFirstHalf("A"))
print(RetainFirstHalf(""))
print(RetainFirstHalf("Hello World"))

print(RetainFirstHalfWithSlice('hippopotamus'))
print(RetainFirstHalfWithSlice("This is the 1st halfThis is the 2nd half"))
print(RetainFirstHalfWithSlice("A"))
print(RetainFirstHalfWithSlice(""))
print(RetainFirstHalfWithSlice("Hello World"))