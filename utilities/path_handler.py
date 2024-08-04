import os


# Ensure the specified directory exists, creating it if necessary
def ensure_directory_exists(directory_path):
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    except PermissionError as e:
        print(
            f"Permission error: Unable to create directory '{directory_path}'. Details: {e}"
        )
        raise
    except OSError as e:
        print(f"OS error: Failed to create directory '{directory_path}'. Details: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

    return directory_path


# Get the path to the images directory, creating it if necessary
def get_images_directory():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    images_dir = os.path.join(current_dir, "..", "database", "images")
    return ensure_directory_exists(images_dir)


# Get the path to the rounds images directory, creating it if necessary
def get_round_images_directory():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    rounds_images_dir = os.path.join(current_dir, "..", "database", "images", "rounds")
    return ensure_directory_exists(rounds_images_dir)


# Get the path to the CSV directory, creating it if necessary
def get_csv_directory():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    csv_dir = os.path.join(current_dir, "..", "database", "csv")
    return ensure_directory_exists(csv_dir)