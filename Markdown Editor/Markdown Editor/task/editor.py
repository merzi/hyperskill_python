from __future__ import annotations


class MarkdownEditor:
    """
    Generator for Markup Code
    """

    help_links = ["https://hyperskill.org/learn/step/13156",
                  "https://hyperskill.org/learn/step/13239",
                  ]

    available_formatter = ["plain", "bold", "italic", "header", "link", "inline-code",
                           "ordered-list", "unordered-list", "new-line", "quote"]
    """
    list of all available formatters
    """

    available_commands = ["!done", "!help", "!example"]
    """
    list of all available commands
    """

    markdown_symbols = {"plain": "",
                        "heading": "#",
                        "bold": "**",
                        "italic": "*",
                        "crossed_out": "~~",
                        "inline-code": "`",
                        "new-line": "\n",
                        "link": {"label_start": "[",
                                 "label_end": "]",
                                 "uri_start": "(",
                                 "uri_end": ")"},
                        "image": {"label_start": "![",
                                  "label_end": "]",
                                  "uri_start": "(",
                                  "uri_end": ")"},
                        "unordered-list": "* ",
                        "ordered-list": "{}. "
                        }
    """
    markdown symbols to generate markdown
    """

    file_name = "output.md"
    """
    filename for the export file
    """

    saved_string: str = ""
    """
    buffer variable for the generated markup code
    """

    def __init__(self: MarkdownEditor) -> None:
        """
        initiate a new instance of the MarkdownEditor Class
        """
        self.menu()

    def menu(self: MarkdownEditor) -> bool:
        """
        executes the menu output and starts the wanted method
        :return: the result of the done method
        """
        command = None
        while command is None:
            command = input("Choose a formatter:")
            if command not in self.available_commands and command not in self.available_formatter:
                command = None
                print("Unknown formatting type or command")
            elif command == "!example":
                self.print_example_text()
                command = None
            elif command == "!help":
                self.print_help()
                command = None
            elif command == "!done":
                return self.save_to_file()
            elif command in self.available_formatter:
                self.run_formatter(command)
                command = None

    def save_to_file(self: MarkdownEditor) -> bool:
        """
        safe the generated code to the file
        :return: True if file has been saved, False if not
        """
        with open(self.file_name, "w", encoding="utf-8") as file_writer:
            file_writer.write(self.saved_string)
            return True
        return False

    def run_formatter(self: MarkdownEditor, formatter: str) -> None:
        """
        search for the wanted formatter and starts him
        :param formatter: the wanted formatter, which should generate the code
        :return: nothing
        """
        if formatter == "header":
            self.print_formatted_heading()
        elif formatter == "image":
            self.print_formatted_image()
        elif formatter == "link":
            self.print_formatted_link()
        elif formatter in ["quote"]:
            self.print_formatted_single_markdown(formatter)
        elif formatter == "new-line":
            self.print_formatted_new_line()
        elif formatter in ["ordered-list", "unordered-list"]:
            self.print_formatted_list(formatter)
        else:
            self.print_formatted_simple(formatter)

    def print_formatted_single_markdown(self: MarkdownEditor, formatter: str) -> str:
        """
        prints the result of the single formatter
        :param formatter: the wanted formatter, which should generate the code
        :return: nothing
        """
        self.saved_string += self.single_formatter(formatter)
        print(self.saved_string)

    def single_formatter(self: MarkdownEditor, formatter: str) -> str:
        """
        ask for the text which will be formatted with the single formatting options
        :param formatter: the wanted formatter, which should generate the code
        :return: the formatted string
        """
        text = input("Text:")
        end_text = ""
        if formatter in ["quote"]:
            end_text = "\n"

        return "{}{}{}".format(self.markdown_symbols[formatter], text, end_text)

    def print_formatted_simple(self: MarkdownEditor, formatter: str) -> None:
        """
        prints the result of the simple formatter and saves it to the string buffer
        :param formatter: the wanted formatter, which should generate the code
        :return: nothing
        """
        self.saved_string += self.simple_formatter(formatter)
        print(self.saved_string)

    def simple_formatter(self: MarkdownEditor, formatter: str) -> str:
        """
        ask for the text which will be formatted with the simple formatting options
        :param formatter: the wanted formatter, which should generate the code
        :return: the formatted string
        """
        text = input("Text:")
        return "{}{}{}".format(self.markdown_symbols[formatter], text, self.markdown_symbols[formatter])

    def print_formatted_heading(self: MarkdownEditor) -> None:
        """
        prints the result of the heading formatter and saves it to the string buffer
        :return: nothing
        """
        self.saved_string += self.heading_formatter()
        print(self.saved_string)

    def heading_formatter(self: MarkdownEditor) -> str:
        """
        ask for the text to be formatted and the level of the heading. Then the headings are formatted.
        :return: the formatted string
        """
        level = None
        while level is None:
            try:
                level = int(input("Level:"))
                if level not in range(1, 7):
                    raise ValueError()
            except ValueError:
                print("The level should be within the range of 1 to 6")
                level = None

        text = input("Text:")
        return "{} {}\n".format(self.markdown_symbols["heading"] * level, text)

    def print_formatted_link(self: MarkdownEditor) -> None:
        """
        prints the result of the link formatter and saves it to the string buffer
        :return: noting
        """
        self.saved_string += self.link_formatter()
        print(self.saved_string)

    def link_formatter(self: MarkdownEditor) -> str:
        """
        ask for the label and the uri for the link. Then the link are formatted
        :return: the formatted string
        """
        label = input("Label:")
        url = input("URL:")

        return "{}{}{}{}{}".format(self.markdown_symbols["link"]["label_start"], label,
                                   self.markdown_symbols["link"]["label_end"] +
                                   self.markdown_symbols["link"]["uri_start"], url,
                                   self.markdown_symbols["link"]["uri_end"])

    def print_formatted_image(self: MarkdownEditor) -> None:
        """
        prints the result of the image formatter and saves it to the string buffer
        :return: nothing
        """
        self.saved_string += self.image_formatter()
        print(self.saved_string)

    def image_formatter(self: MarkdownEditor) -> str:
        """
        ask for the alternate Text and the source for the image. Then the image will be formatted
        :return: the formatted string
        """
        alt_text = input("alternate text:")
        src = input("URL")

        return "{}{}{}{}{}".format(self.markdown_symbols["image"]["label_start"], alt_text,
                                   self.markdown_symbols["image"]["label_end"] +
                                   self.markdown_symbols["image"]["uri_start"], src,
                                   self.markdown_symbols["image"]["uri_end"])

    def print_formatted_new_line(self: MarkdownEditor) -> None:
        """
        prints the result of the new line formatter and saves it to the string buffer
        :return: nothing
        """
        self.saved_string += self.new_line_formatter()
        print(self.saved_string)

    def new_line_formatter(self: MarkdownEditor) -> str:
        """
        creates an empty line
        :return: the formatted string
        """
        return "{}".format(self.markdown_symbols["new-line"])

    def print_formatted_list(self: MarkdownEditor, formatter: str) -> None:
        """
        prints the result of the list formatter and saves it to the string buffer
        :param formatter: type of the list (ordered or unordered)
        :return: nothing
        """
        self.saved_string += self.list_formatter(formatter) + "\n"
        print(self.saved_string)

    def list_formatter(self: MarkdownEditor, formatter: str) -> str:
        """
        Ask for the amount of list items and for the list items. Then the list will be format the list and return them
        :param formatter: type of the list (ordered or unordered)
        :return: the formatted string
        """
        num_rows = None
        while num_rows is None:
            try:
                num_rows = int(input("Number of rows:"))
                if num_rows <= 0:
                    raise ValueError()
            except ValueError:
                print("The number of rows should be greater than zero")
                num_rows = None
        row_text = [input("Row #{}".format(num + 1)) for num in range(0, num_rows)]
        buffer_list: list
        template_string = "{}{}"
        if formatter == "ordered-list":
            template_string = template_string.format(self.markdown_symbols[formatter], "{}")
            buffer_list = list(map(lambda entry: template_string.format(entry[0] + 1, entry[1]), enumerate(row_text)))
        else:
            buffer_list = list(map(lambda value: template_string.format(self.markdown_symbols[formatter], value),
                                   row_text))
        return "\n".join(buffer_list)

    def print_help(self: MarkdownEditor) -> None:
        """
        prints the help for the program
        :return: nothing
        """
        print("Available formatters: {}".format(" ".join(self.available_formatter)))
        print("Special commands: {}".format(" ".join(self.available_commands)))

    def print_example_text(self: MarkdownEditor) -> None:
        """
        prints some simple example text
        :return: nothing
        """
        print("# John Lennon")
        print("or ***John Winston Ono Lennon*** was one of *The Beatles*.")
        print("Here are the songs he wrote I like the most:")
        print("- Imagine")
        print("- Norwegian Wood")
        print("- Come Together")
        print("- In My Life")
        print("- ~~Hey Jude~~ (that was *McCartney*)")


MarkdownEditor()
