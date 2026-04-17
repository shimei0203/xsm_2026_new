# CSV Cleaner CLI Task

## Task Description
You need to write a Python command-line tool named `cleaner.py` that cleans a dirty CSV file and generates a standardized clean CSV file.

## Input File
- Input: `dirty_data.csv` (contains messy, invalid, and non-standard data)

## Required Cleaning Rules
1. Remove all empty lines and lines with only whitespace
2. Remove rows where the "id" field is empty, non-numeric, or duplicated
3. Standardize the "email" field:
   - Convert all to lowercase
   - Remove any spaces in emails
   - Keep only valid email format (contains @ and domain)
   - Remove rows with invalid emails
4. Clean the "name" field:
   - Remove leading/trailing spaces
   - Capitalize the first letter of each word
5. Remove all special characters (e.g., !@#$%^&*()[]{}|~`<>?) except standard punctuation in name/email
6. The output CSV must keep the header: id,name,email
7. Save the cleaned data to `clean_data.csv`

## Command Usage
The CLI must support:
python cleaner.py --input dirty_data.csv --output clean_data.csv

## Output Requirements
- Generate valid, clean CSV file
- No empty rows
- No duplicate IDs
- All emails valid and lowercase
- Names formatted correctly