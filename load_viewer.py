import csv

LOAD_FILE = "beam_loads.csv"


def display_loads() -> None:
    try:
        with open(LOAD_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No load data found.")
                return

            print("\nBEAM LOAD DATA")
            print("-" * 40)

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("Load data file not found.")
    except OSError as error:
        print(f"Error reading load data file: {error}")


if __name__ == "__main__":
    display_loads()
