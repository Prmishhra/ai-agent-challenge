# AI Agent Challenge – Bank Statement Parser

This project implements a coding agent that can automatically create and run parsers for bank statement PDFs.

## 📂 Project Structure

ai-agent-challenge/
│
├── agent.py # Main agent entrypoint
├── requirements.txt # Python dependencies
├── README.md # Project guide
│
├── data/
│ └── icici/
│ ├── icici_sample.pdf # Sample ICICI input
│ └── result.csv # Expected output
│
├── custom_parsers/
│ ├── parser_template.py # Parser contract (template)
│ ├── icici_parser.py # Custom ICICI parser
│
├── tests/
│ ├── test_icici_parser.py # Test for ICICI parser


## ⚙️ Installation

Clone your fork and install dependencies:

```bash
git clone https://github.com/Prmishhra/ai-agent-challenge.git
cd ai-agent-challenge
pip install -r requirements.txt

## Usage
Run on ICICI sample statement

python agent.py --bank icici --pdf data/icici/icici_sample.pdf --out icici_output.csv

This will parse the PDF and write the output to icici_output.csv.

## Run for a new bank (e.g., SBI)

python agent.py --bank sbi --pdf data/sbi/sbi_sample.pdf --out sbi_output.csv

If no parser exists yet, agent.py will auto-generate custom_parsers/sbi_parser.py as a template.

🧪 Running Tests

pytest -v