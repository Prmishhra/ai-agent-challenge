import argparse
import os
from pathlib import Path
import importlib.util
import pandas as pd

TEMPLATE_CODE = """\
import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    \"\"\"
    Auto-generated parser for {bank_name}.
    Args:
        pdf_path (str): Path to the PDF bank statement.
    Returns:
        pd.DataFrame with columns: Date, Description, Debit Amt, Credit Amt, Balance
    \"\"\"
    # TODO: Implement parsing logic for {bank_name} statements
    raise NotImplementedError("Parser for {bank_name} not implemented yet.")
"""

def create_parser_file(bank_name: str):
    file_path = Path(f"custom_parsers/{bank_name}_parser.py")
    if file_path.exists():
        print(f"✅ Parser already exists: {file_path}")
        return file_path

    # Write template parser
    with open(file_path, "w") as f:
        f.write(TEMPLATE_CODE.format(bank_name=bank_name.capitalize()))

    print(f"🆕 Created parser: {file_path}")
    return file_path

def run_parser(bank_name: str, pdf_path: str, output_csv: str):
    module_name = f"custom_parsers.{bank_name}_parser"
    spec = importlib.util.spec_from_file_location(module_name, f"custom_parsers/{bank_name}_parser.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Call the parse function
    df = module.parse(pdf_path)
    df.to_csv(output_csv, index=False)
    print(f"✅ Extracted data written to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bank Statement Parser Agent")
    parser.add_argument("--bank", required=True, help="Bank name (e.g., icici, sbi, hdfc)")
    parser.add_argument("--pdf", required=True, help="Path to the input PDF file")
    parser.add_argument("--out", default="output.csv", help="Path to save extracted CSV")

    args = parser.parse_args()

    # Step 1: Ensure parser file exists
    parser_file = create_parser_file(args.bank.lower())

    # Step 2: Run the parser
    run_parser(args.bank.lower(), args.pdf, args.out)