from pathlib import Path

from python_data_processing_toolkit.loader import load_text
from python_data_processing_toolkit.normalizer import normalize
from python_data_processing_toolkit.filters import filter_equals

def main():
    path = Path("examples/people.csv")
    
    raw_data = load_text(path)
    records = normalize(raw_data)
    filtered = filter_equals(records, "city", "Moscow")
    
    print(filtered)

if __name__ == "__main__":
    main()