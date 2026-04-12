from etl.extract import extract
from etl.transform import transform
from etl.load import load

def main():
    df = extract()
    df = transform(df)
    load(df)
    print(df.head())

if __name__ == "__main__":
    main()