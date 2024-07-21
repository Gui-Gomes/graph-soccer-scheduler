import csv

# Read lines from a CSV file
def read_csv(file_path):
    data = []
    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                data.append(row)  # Add the row as is
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        raise IOError(f"Error opening the file '{file_path}': {e.strerror}")
    except csv.Error as e:
        raise csv.Error(f"Error reading the CSV file '{file_path}': {e}")
    except Exception as e:
        raise Exception(f"Unexpected error while reading the file '{file_path}': {e}")
    return data
