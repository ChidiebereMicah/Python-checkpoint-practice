def RetainFirstHalf(text):
    text_len = len(text)
    half_len = int(text_len/2)
    #output = ''
    if text == '':
        return ''
    elif text_len == 1:
        return text
    else:
        for i in range(half_len):
            output = output + text[i]
    return output

print(RetainFirstHalf('hippopotamus'))