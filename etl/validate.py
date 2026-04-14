def validate(df):
    print("Validating data...")

    # check nulls
    null_count = df.isnull().sum().sum()
    if null_count > 0:
        print(f"Warning: {null_count} null values found")

    # check duplicates
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        print(f"Warning: {dup_count} duplicate rows found")

    print("Validation completed")
    return df
