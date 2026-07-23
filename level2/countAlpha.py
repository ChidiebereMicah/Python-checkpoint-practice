def CountAlpha(text):
    count = 0
    for ch in text:
        if ch.isalpha():
            count += 1
    return count

def main():
    print(CountAlpha("Hello world"))
    print(CountAlpha("H e l l o"))
    print(CountAlpha("H1e2l3l4o"))
    print(CountAlpha(""))

if __name__ == "__main__":
    main()