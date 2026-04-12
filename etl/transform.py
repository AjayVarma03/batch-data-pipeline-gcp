import pandas as pd

def transform(df):
    print("Starting transformation...")

    # 1. Remove nulls
    df = df.dropna()

    # 2. Remove duplicates
    df = df.drop_duplicates()

    # 3. Create new column (business logic)
    df["amount_with_tax"] = df["amount"] * 1.18

    # 4. Standardize text
    df["product"] = df["product"].str.lower()
    df["city"] = df["city"].str.title()

    print("Transformation completed")

    return df