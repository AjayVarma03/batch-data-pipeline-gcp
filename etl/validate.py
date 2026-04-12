def validate(df):
    print("Validating data...")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values found")

    if df.duplicated().sum() > 0:
        raise ValueError("Duplicates found")

    return df