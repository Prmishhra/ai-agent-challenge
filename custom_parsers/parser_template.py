"""
Parser Template
---------------
All custom bank parsers must implement the `parse(pdf_path)` function
that reads a PDF statement and returns a pandas DataFrame.

The DataFrame schema must match the expected CSV file for that bank.
"""

import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    """
    Parse a bank statement PDF into a pandas DataFrame.

    Parameters
    ----------
    pdf_path : str
        Path to the PDF bank statement.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the parsed statement,
        with schema matching the provided CSV.
    """
    # Placeholder: return empty DataFrame for now
    # The agent will replace this with real parsing logic.
    return pd.DataFrame()