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


def add_line_break(sentence):
    ix = sentence.index("।")
    l1 = sentence[:ix+2]
    l2 = sentence[ix+2:]
    return l1 + "<br>" + l2


def process_data(data):
    shlokas = [add_line_break(shloka) for shloka in data["shlokas"]]
    return {"shlokas": shlokas}


if __name__ == '__main__':

    template = get_template()
    data = get_data("data.json")
    data = process_data(data)

    with open("index.html", "w") as f:
        f.write(template.render(**data))

