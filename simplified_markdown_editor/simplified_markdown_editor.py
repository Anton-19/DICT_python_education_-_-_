def print_help():
    # Вивід доступних форматерів та спеціальних команд
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def apply_format(formatter, text):
    # Застосування форматування до тексту
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "header":
        while True:
            try:
                level = int(input("Level: > "))
                if 1 <= level <= 6:
                    return f"{'#' * level} {text}\n"
                else:
                    print("The level should be within the range of 1 to 6.")
            except ValueError:
                print("The level should be within the range of 1 to 6.")
    elif formatter == "link":
        url = input("URL: > ")
        return f"[{text}]({url})"
    elif formatter == "new-line":
        return "\n\n"
    return text


def apply_list(formatter):
    # Форматування списків
    while True:
        try:
            num_rows = int(input("Number of rows: > "))
            if num_rows <= 0:
                print("The number of rows should be greater than zero.")
            else:
                break
        except ValueError:
            print("The number of rows should be greater than zero.")

    list_items = []
    for i in range(1, num_rows + 1):
        item = input(f"Row #{i}: > ")
        if formatter == "ordered-list":
            list_items.append(f"{i}. {item}")
        else:
            list_items.append(f"* {item}")

    return "\n" + "\n".join(list_items) + "\n\n"


def main():
    # Набір доступних форматерів
    available_formatters = {"plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                            "unordered-list", "new-line"}
    # Набір спеціальних команд
    special_commands = {"!help", "!done"}
    markdown_text = ""

    while True:
        # Запт користувача на вибір форматера
        user_input = input("Choose a formatter: > ")

        if user_input == "!help":
            print_help()
        elif user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(markdown_text)
            print(markdown_text)
            break
        elif user_input in available_formatters:
            if user_input == "new-line":
                markdown_text += "\n\n"
            elif user_input == "header":
                while True:
                    try:
                        level = int(input("Level: > "))
                        if 1 <= level <= 6:
                            text = input("Text: > ")
                            markdown_text += f"{'#' * level} {text}\n"
                            break
                        else:
                            print("The level should be within the range of 1 to 6.")
                    except ValueError:
                        print("The level should be within the range of 1 to 6.")
            elif user_input == "link":
                label = input("Label: > ")
                url = input("URL: > ")
                markdown_text += f"[{label}]({url})"
            elif user_input in {"ordered-list", "unordered-list"}:
                markdown_text += apply_list(user_input)
            else:
                text = input("Text: > ")
                markdown_text += apply_format(user_input, text) + " "
            print(markdown_text)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()


