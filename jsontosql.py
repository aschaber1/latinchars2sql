#!/usr/bin/env python3

import json

json_file = open("json")
data = json.load(json_file)

for entry in data:
    print(f"INSERT into TABLE1 (codepoint, char) VALUES (\"{entry['codepoint']}\", \"{entry['char']}\");")

