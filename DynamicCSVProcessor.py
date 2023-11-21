import pandas as pd

def identify_static_columns(df):
    static_columns = []
    for column in df.columns:
        if df[column].nunique() == 1:
            static_columns.append(column)
    return static_columns

def remove_static_columns(df, static_columns):
    return df.drop(columns=static_columns)

def main(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Identify static columns
    static_columns = identify_static_columns(df)

    # Remove static columns
    dynamic_df = remove_static_columns(df, static_columns)

    # Write the dynamic DataFrame to a new CSV file
    dynamic_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "input.csv"  # Replace with your input CSV file
    output_file = "output.csv"  # Replace with your desired output CSV file

    main(input_file, output_file)
