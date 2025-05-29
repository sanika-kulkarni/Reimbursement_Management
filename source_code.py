'''
Approach :
Step 1.Data Ingestion and Structuring: The TariffSage class initializes by reading CSV/JSON tariff files using Pandas, concatenating them into a single DataFrame (self.tariff_knowledge) for easy data manipulation.
Step 2.Basic Keyword Retrieval: The consult_the_sage method takes a user query, converts it to lowercase, and then uses Pandas' apply function with a lambda to check if any word from the query exists (case-insensitively) in any cell of the tariff_knowledge DataFrame.
Step 3.Result Presentation: If relevant rows are found based on the keyword search, the top few matching rows are returned as a Pandas DataFrame, representing the Sage's "insights."
Step 4.Fuzzy Matching (Optional Enhancement): If no direct keyword match is found, the (optional) _gentle_suggestion method uses the fuzzywuzzy library to find the closest matching description in the tariff data, offering a potential correction to the user's query.
Step 5.Simple Query Handling Loop: The if __name__ == "__main__": block creates an instance of TariffSage, takes user input in a loop, calls consult_the_sage to get a response, and prints the result.
'''
import pandas as pd
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class TariffSage:
    def __init__(self, tariff_files):
        self.tariff_knowledge = self._ingest_and_structure_data(tariff_files)

    def _ingest_and_structure_data(self, tariff_files):
        print("The Tariff Sage is now absorbing the ancient scrolls...")
        combined_data = []
        for file_path in tariff_files:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
                combined_data.append(df)
                print(f"  ...processed '{file_path}'.")
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                df = pd.DataFrame(data)
                combined_data.append(df)
                print(f"  ...deciphered '{file_path}'.")
            elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
                try:
                    df = pd.read_excel(file_path)
                    combined_data.append(df)
                    print(f"  ...transcribed '{file_path}'.")
                except Exception as e:
                    print(f"Error reading Excel file '{file_path}': {e}")
            else:
                print(f"Warning: Skipping unsupported file type '{file_path}'.")
        master_tariff = pd.concat(combined_data, ignore_index=True)
        print("The Sage has integrated the knowledge.")
        return master_tariff

    def consult_the_sage(self, query):
        print(f"\nSeeking guidance on: '{query}'...")
        query = query.lower()
        relevant_insights = self.tariff_knowledge[self.tariff_knowledge.apply(lambda row: any(keyword in row.astype(str).str.lower().values for keyword in query.split()), axis=1)]
        if not relevant_insights.empty:
            print("The Sage offers these insights:")
            return relevant_insights.head()
        else:
            print("The Sage strains to find an answer...")
            best_match, score = self._gentle_suggestion(query, self.tariff_knowledge['description'].astype(str).tolist())
            if score > 80 and best_match:
                return f"Perhaps you were inquiring about: '{best_match}'?"
            return "The Sage finds no direct answer to your query."

    def _gentle_suggestion(self, query, choices):
        if choices:
            return process.extractOne(query, choices)
        return None, 0

if __name__ == "__main__":
    # Now you can directly use your .xls or .xlsx file paths here
    tariff_files = ['path/to/your_first_excel_file.xlsx',
                    'path/to/your_second_excel_file_sheet1.xlsx',
                    'path/to/your_second_excel_file_sheet2.xlsx'] # Example

    the_sage = TariffSage(tariff_files)

    while True:
        user_query = input("Consult The Tariff Sage (or type 'exit'): ")
        if user_query.lower() == 'exit':
            print("The Tariff Sage bids you farewell.")
            break
        guidance = the_sage.consult_the_sage(user_query)
        print(guidance)
        print("-" * 40)
