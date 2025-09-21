# """
# ICICI Bank Statement Parser
# ---------------------------
# Parses ICICI bank statement PDF into a pandas DataFrame.

# Contract:
# ---------
# parse(pdf_path: str) -> pd.DataFrame

# Output schema must match the provided CSV (data/icici/icic_sample.csv).
# """

# import pdfplumber
# import pandas as pd
# import re


# def parse(pdf_path: str) -> pd.DataFrame:
#     rows = []

#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text()
#             if not text:
#                 continue

#             for line in text.splitlines():
#                 # 🔹 Example heuristic parsing for ICICI statements
#                 # Adjust regex according to actual PDF format
#                 match = re.match(r"(\d{2}-\d{2}-\d{4})\s+(.+?)\s+([\d,]+\.\d{2})", line)
#                 if match:
#                     date = match.group(1)
#                     description = match.group(2).strip()
#                     amount = match.group(3).replace(",", "")

#                     rows.append({
#                         "Date": date,
#                         "Description": description,
#                         "Amount": float(amount)
#                     })

#     df = pd.DataFrame(rows)

#     return df

import pdfplumber
import pandas as pd
import re

def parse(pdf_path: str) -> pd.DataFrame:
    rows = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            for line in text.splitlines():
                # Skip the header row
                if line.strip().startswith("Date Description"):
                    continue

                # Regex: Date | Description | Amount | Balance
                match = re.match(
                    r"(\d{2}-\d{2}-\d{4})\s+(.+?)\s+([\d,.]+)\s+([\d,.]+)$",
                    line
                )
                if not match:
                    # Debug unparsed lines
                    # print("❌ No match:", line)
                    continue

                date = match.group(1)
                description = match.group(2).strip()
                amount = match.group(3).replace(",", "")
                balance = match.group(4).replace(",", "")

                # Decide Debit vs Credit based on description
                description_lower = description.lower()
                debit_amt, credit_amt = "", ""

                # Rules to decide Debit vs Credit (based on your CSV)
                # Money IN → Credit
                if any(word in description_lower for word in ["salary", "deposit", "interest", "refund"]):
                    credit_amt = amount
                # Money OUT → Debit
                else:
                    debit_amt = amount



                rows.append([date, description, debit_amt, credit_amt, balance])

    return pd.DataFrame(rows, columns=["Date", "Description", "Debit Amt", "Credit Amt", "Balance"])