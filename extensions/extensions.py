#extension file lab


def main():
    i = str(input("File name: ")).strip().lower()
    if i.endswith(".gif") == True:
        print("image/gif")
    elif i.endswith(".jpg") or i.endswith(".jpeg") == True:
        print("image/jpeg")
    elif i.endswith(".png") == True:
        print("image/png")
    elif i.endswith(".pdf") == True:
        print("application/pdf")
    elif i.endswith(".txt") == True:
        print("text/plain")
    elif i.endswith(".zip") == True:
        print("application/zip")
    else:
        print("application/octet-stream")


main()