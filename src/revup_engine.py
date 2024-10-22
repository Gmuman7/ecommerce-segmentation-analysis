import pandas as pd

def load_data(file_path):
    """
    Load the e-commerce dataset from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Perform basic data cleaning and preprocessing.
    """
    # Remove rows with missing CustomerID as they cannot be segmented
    data_cleaned = data.dropna(subset=['CustomerID'])
    
    # Create a TotalPrice column for Revenue calculation
    data_cleaned['TotalPrice'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']
    
    print("Data cleaned successfully.")
    return data_cleaned

if __name__ == "__main__":
    file_path = 'data/dataset.csv'
    data = load_data(file_path)
    if data is not None:
        cleaned_data = preprocess_data(data)
