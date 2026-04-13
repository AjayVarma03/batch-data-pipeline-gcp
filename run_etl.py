import logging
import os

os.makedirs('logs', exist_ok=True)

log_file = os.path.join(os.getcwd(), 'logs', 'pipeline.log')

# 🔥 force reset
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("Log file path:", log_file)

logging.info("===== PIPELINE STARTED =====")
from etl.extract import extract
from etl.transform import transform
from etl.load import load, run_merge
from etl.validate import validate


# ✅ pipeline execution
df = extract()
df = validate(df)
df = transform(df)
load(df)
