import logging
import csv

# Correct logging setup with valid field names
logging.basicConfig(
    filename="file.log",
    filemode="a",
    format="{asctime} - {name} - {levelname} - {message}",
    style="{",
    level=logging.DEBUG
)


def logging_system(filename):
    logging.info("Logging system started")
    try:
        with open(filename, "r") as file:
            content = csv.reader(file)
            next(content)  # Skip header
            for row in content:
                try:
                    name = row[0]
                    age = int(row[1])  # May raise ValueError
                    logging.info(f"Name: {name}, Age: {age}")
                except ValueError:
                    logging.error(f"Invalid age for {row[0]}: {row[1]}")
    except FileNotFoundError:
        logging.error("File not found!")


# Call function with correct file name
logging_system("afile.csv")

# Log a debug message at the end
logging.debug("Files are analyzed for correct function")
