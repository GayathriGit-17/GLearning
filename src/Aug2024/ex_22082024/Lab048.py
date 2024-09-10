# match
browser=input("Enter browser name\n")
browser=browser.lower()
match browser:

    case "chrome":
        print("Chrome")
    case "firefox":
        print("Firefox")
    case "mozilla":
        print("mozila")
    case "apple" | "edge":
        print("Browser is apple /edge")
    case _:
        print("Browser not found ")

