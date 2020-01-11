import json
from jinja2 import Environment, FileSystemLoader


def get_template():
    loader = FileSystemLoader(searchpath='./')
    env = Environment(loader=loader)
    template = env.get_template("template.html")
    return template


def get_data(fname):
    with open(fname, "r") as f:
        data = json.load(f)
    return data


if __name__ == '__main__':

    template = get_template()
    data = get_data("data.json")

    with open("index.html", "w") as f:
        f.write(template.render(**data))

