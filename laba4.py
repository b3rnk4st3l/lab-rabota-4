import json
import xml.etree.ElementTree as ET

def convert_to_json(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = []
    for person in root:
        person_data = {}
        for element in person:
            person_data[element.tag] = element.text
        data.append(person_data)

    with open("data.json", "w") as f:
        json.dump(data, f)

convert_to_json("data.xml")