def PrintIfNot(text):
    if len(text) < 3:
        return "G\n"
    return "Invalid input\n"

def main():
    print(PrintIfNot("abcdefz"))
    print(PrintIfNot("abc"))
    print(PrintIfNot(""))
    print(PrintIfNot("14"))

if __name__ == "__main__":
    main()