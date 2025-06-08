import json
import logging
logging.basicConfig(filename="data.log", filemode='w',
                    format='{levelname}-{message}', style="{",
                    level=logging.INFO)


def read_json(filename):
    logging.info("Logging_system for json file")
    try:
        with open("myfile.json", "r") as file:
            content = json.load(file)
            logging.info("Json file opened successfully")
            for item in content:
                try:
                    age = int(item["age"])
                    logging.info(f"{item['name']} age is {age}")
                except ValueError:
                    logging.error(f"Invalid age of {item['name']}")
    except FileNotFoundError:
        logging.error(f"File not found")


read_json("myfile.json")
