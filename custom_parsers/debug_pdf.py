import pandas as pd
from custom_parsers.icici_parser import parse

if __name__ == "__main__":
    pdf_path = "data/icici/icici_sample.pdf"
    output_csv = "data/icici/parsed_from_pdf.csv"

    # Run the parser
    df = parse(pdf_path)

    # Show first few rows
    print("\n--- Extracted DataFrame ---\n")
    print(df)

    # Save to CSV for manual comparison
    df.to_csv(output_csv, index=False)
    print(f"\nExtracted data saved to: {output_csv}")