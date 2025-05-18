import pandas as pd

def main():
    # Read the Parquet file
    parquet_path = "../MLFlow/data/Benign-Monday-no-metadata.parquet"
    df = pd.read_parquet(parquet_path)
    
    # Print the schema
    print("\nSchema of the Parquet file:")
    print("=" * 50)
    print(df.dtypes)
    
    # Print a sample of the data
    print("\nSample data (first 5 rows):")
    print("=" * 50)
    print(df.head())

if __name__ == "__main__":
    main()
