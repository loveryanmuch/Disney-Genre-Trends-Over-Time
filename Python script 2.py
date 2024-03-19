import pandas as pd

def load_and_process_data(file_path):
    """
    Loads the Disney movies dataset and performs basic processing.

    Parameters:
    - file_path: str, the path to the CSV file containing the data.

    Returns:
    - df: pandas.DataFrame, the processed dataset.
    """
    # Load the data
    df = pd.read_csv(file_path)

    # Convert 'release_date' to datetime format
    df['release_date'] = pd.to_datetime(df['release_date'])

    # Extract year from 'release_date'
    df['year'] = df['release_date'].dt.year

    return df

if __name__ == "__main__":
    # Example usage
    file_path = 'data/disney_movies_total_gross.csv'
    disney_data = load_and_process_data(file_path)
    print(disney_data.head())
    
