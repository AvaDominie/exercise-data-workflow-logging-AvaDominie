import polars as pl
import logging
import os



logger = logging.getLogger('my_app')
logger.setLevel(level=logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



def get_file_size(file_path: str) -> float:
    # Return the size of the file in KB
    return os.path.getsize(file_path) / 1024


def read_parquet(file_path: str) -> "pl.DataFrame":
    # Read a parquet file into a Polars DataFrame
    try:
        df = pl.read_parquet(file_path)
        return df
    except Exception as e:
        print(f"Error reading parquet file: {e}")
        return None



def get_data_info(df: "pl.DataFrame") -> dict:
    # Return a dictionary with data info: shape, schema, etc.
    if df is not None:
        return {
            "shape": df.shape,
            "schema": df.schema,
            "columns": df.columns,
            "rows": df.rows,
        }
    else:
        return {"error": "DataFrame is None"}



def save_to_csv(df: "pl.DataFrame", output_path: str):
    # Save DataFrame as CSV
    try:
        df.write_csv(output_path)
        print(f"DataFrame saved to {output_path}")
    except Exception as e:
        print(f"Error saving DataFrame to CSV: {e}")
    




def main():
    # Example usage with logging and comments
    # check if sample.parquet exists, then process
    file_path = 'droids.parquet'
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return
    
    # 1. Get and print the file size
    file_size = get_file_size(file_path)
    logger.info(f"File size of {file_path}: {file_size:.2f} KB")
    # 2. Read parquet into DataFrame
    df = read_parquet(file_path)
    logger.info(f"DataFrame loaded from {file_path}")   
    # 3. Get and print info about the data
    data_info = get_data_info(df)
    logger.info(f"DataFrame info: {data_info}")
    # 4. Save DataFrame to CSV
    output_path = 'droids.csv'
    save_to_csv(df, output_path)

    logger.info(f"DataFrame saved to {output_path}")

    return df

if __name__ == "__main__":

    main()
