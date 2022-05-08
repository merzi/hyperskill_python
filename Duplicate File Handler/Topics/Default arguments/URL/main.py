import string


def create_url(host="localhost", port=443):
    url_template = string.Template("https://$host:$port")
    return url_template.substitute(host=host, port=port)
