from etl.validate import validate
from etl.extract import extract
from etl.transform import transform
from etl.load import load, run_merge

df = extract()
df = validate(df)
df = transform(df)
load(df)
run_merge()