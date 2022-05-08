import string


def print_book_info(title, author=None, year=None):
    base_template = string.Template("$title$extension")
    extension_template = string.Template(" was written $ext")
    title_template = string.Template('"$title"')
    written_by = string.Template("by $author")
    written_in = string.Template("in $year")
    #  Write your code here
    extension = ""
    if author is not None and year is not None:
        ext = written_by.substitute(author=author) + " " + written_in.substitute(year=year)
        extension = extension_template.substitute(ext=ext)
    elif author is not None and year is None:
        auth = written_by.substitute(author=author)
        extension = extension_template.substitute(ext=auth)
    elif author is None and year is not None:
        ye = written_in.substitute(year=year)
        extension = extension_template.substitute(ext=ye)

    title_str = title_template.substitute(title=title)
    print(base_template.substitute(title=title_str, extension=extension))
