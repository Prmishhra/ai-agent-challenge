import pandas as pd
from custom_parsers.icici_parser import parse

def test_icici_parser_structure():
    df = parse("data/icici/icici_sample.pdf")

    # 1. Parser returns a DataFrame
    assert isinstance(df, pd.DataFrame), "Parser did not return a DataFrame"

    # 2. Check expected columns
    expected_columns = ["Date", "Description", "Debit Amt", "Credit Amt", "Balance"]
    assert list(df.columns) == expected_columns, f"Expected columns {expected_columns}, got {list(df.columns)}"

    # 3. Ensure DataFrame is not empty
    assert len(df) > 0, "Parsed DataFrame is empty"

    # 4. Ensure at least one Debit or Credit value is present
    assert (df["Debit Amt"].astype(str) != "").any() or (df["Credit Amt"].astype(str) != "").any(), \
        "No Debit or Credit values found in parsed DataFrame"