from pathlib import Path

from python_data_processing_toolkit.loader import load_text
from python_data_processing_toolkit.normalizer import normalize

def main():
    path = Path("examples/people.csv")
    
    raw_data = load_text(path)
    records = normalize(raw_data)
    
    print(records)

if __name__ == "__main__":
    main()