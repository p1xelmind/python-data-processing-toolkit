from pathlib import Path

from python_data_processing_toolkit.loader import load_text

def main():
    path = Path("examples/people.csv")
    text = load_text(path)
    print(text)

if __name__ == "__main__":
    main()