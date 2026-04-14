def validate(df):
    print("Validating data...")

    # check if dataframe is empty
    if df.empty:
        raise ValueError("DataFrame is empty")

    print("Columns:", df.columns.tolist())

    # null check (safe for any schema)
    if df.isnull().sum().sum() > 0:
        print("Warning: Null values found")

    # duplicate check
    if df.duplicated().sum() > 0:
        print("Warning: Duplicate rows found")

    print("Validation completed")
    return df
