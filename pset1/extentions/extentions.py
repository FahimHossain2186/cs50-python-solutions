def main():
    x = input("File name: ")
    x = x.lower().strip().split(".")

    print(extentions(x[-1]))

def extentions(x):
    match x:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()