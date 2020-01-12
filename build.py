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


def split_to_lines(shloka):
    ix = shloka.index("।")
    l1 = shloka[:ix + 2]
    l2 = shloka[ix + 2:]
    return [l1,l2]


def split_to_words(shloka):
    shloka_ = []
    for line in shloka:
        shloka_.append(line.split(" "))
    return shloka_


def process_data(data):
    shlokas = data["shlokas"]
    shlokas = map(split_to_lines, shlokas)
    shlokas = map(split_to_words, shlokas)
    return {"shlokas": shlokas}


if __name__ == '__main__':

    template = get_template()
    data = get_data("data.json")
    data = process_data(data)

    with open("index.html", "w") as f:
        f.write(template.render(**data))

