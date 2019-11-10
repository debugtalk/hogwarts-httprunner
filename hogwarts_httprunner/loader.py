import yaml


def load_yaml(yml_file):
    with open(yml_file, "r", encoding='utf-8') as f:
        yml_content = f.read()
        loaded_json = yaml.load(yml_content)

    return loaded_json
