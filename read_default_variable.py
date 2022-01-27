import json
def read(file):
    f = open(file, 'r')
    content = f.read()
    variables = json.loads(content)
    f.close()
    return variables