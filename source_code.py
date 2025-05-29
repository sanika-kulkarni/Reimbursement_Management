'''
Approach :
1: Reads Files: The program opens and reads your price list files (like Excel sheets provided in the given assignment).
2.Remembers Data: It puts all the info from those files into its memory.
3.Listens to You: You type a question about prices.
4.Searches Memory: It looks for words from your question in the price info.
5.Tells You Answer: It shows you the prices it found that match your question. If it's not sure, it might guess what you meant.
'''
import pandas as pd # For data manipulation and reading files
import json # For handling JSON data
from fuzzywuzzy import fuzz # For fuzzy string matching
from fuzzywuzzy import process # For extracting the best fuzzy match

class TariffSage:
    """
    A class representing the Tariff Sage, an AI assistant for querying tariff data.
    """
    def __init__(self, tariff_files):
        """
        Initializes the TariffSage by loading and structuring data from the provided files.

        Args:
            tariff_files (list): A list of file paths to tariff data files (CSV, JSON, XLS, XLSX).
        """
        self.tariff_knowledge = self._ingest_and_structure_data(tariff_files)

    def _ingest_and_structure_data(self, tariff_files):
        """
        Loads and combines data from different tariff files into a single Pandas DataFrame.

        Args:
            tariff_files (list): A list of file paths.

        Returns:
            pandas.DataFrame: A DataFrame containing the combined tariff data.
        """
        print("The Tariff Sage is now absorbing the ancient scrolls...")
        combined_data = [] # Initialize an empty list to store DataFrames
        for file_path in tariff_files:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path) # Read CSV file into a DataFrame
                combined_data.append(df) # Add the DataFrame to the list
                print(f"  ...processed '{file_path}'.")
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data = json.load(f) # Load JSON data from the file
                df = pd.DataFrame(data) # Convert JSON data to a DataFrame
                combined_data.append(df) # Add the DataFrame to the list
                print(f"  ...deciphered '{file_path}'.")
            elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
                try:
                    df = pd.read_excel(file_path) # Read Excel file into a DataFrame
                    combined_data.append(df) # Add the DataFrame to the list
                    print(f"  ...transcribed '{file_path}'.")
                except Exception as e:
                    print(f"Error reading Excel file '{file_path}': {e}")
            else:
                print(f"Warning: Skipping unsupported file type '{file_path}'.")
        master_tariff = pd.concat(combined_data, ignore_index=True) # Concatenate all DataFrames into one
        print("The Sage has integrated the knowledge.")
        return master_tariff

    def consult_the_sage(self, query):
        """
        Processes a user query to find relevant information in the tariff data.

        Args:
            query (str): The user's natural language query.

        Returns:
            pandas.DataFrame or str: The top matching tariff entries or a message if no match is found.
        """
        print(f"\nSeeking guidance on: '{query}'...")
        query = query.lower() # Convert query to lowercase for case-insensitive search
        # Apply a function to each row to check if any keyword from the query exists in the row (converted to string and lowercase)
        relevant_insights = self.tariff_knowledge[self.tariff_knowledge.apply(lambda row: any(keyword in row.astype(str).str.lower().values for keyword in query.split()), axis=1)]
        if not relevant_insights.empty:
            print("The Sage offers these insights:")
            return relevant_insights.head() # Return the top few matching results
        else:
            print("The Sage is trying to find the best answer...")
            # Attempt to find a similar entry using fuzzy matching
            best_match, score = self._gentle_suggestion(query, self.tariff_knowledge['description'].astype(str).tolist())
            if score > 80 and best_match:
                return f"Were you trying to enquire about: '{best_match}'?"
            return "The Sage finds no direct answer to your query."

    def _gentle_suggestion(self, query, choices):
        """
        Provides a fuzzy match suggestion for the user's query if no direct match is found.

        Args:
            query (str): The user's query.
            choices (list): A list of strings to compare the query against (e.g., procedure descriptions).

        Returns:
            tuple: The best matching string and its similarity score, or (None, 0) if no choices are provided.
        """
        if choices:
            return process.extractOne(query, choices) # Find the single best match
        return None, 0

if __name__ == "__main__":
    # Define the list of tariff files to be loaded
    tariff_files = ['OPCS code - opcs4-8_toce_analysis_nov_2016_v1_0.xls',
                    'ICD 10 - Codes_Jan2025.xlsx',
                    'HRG Codes - 22-23NT_Annex-A-National-tariff-workbook_Apr22.xlsx']

    the_sage = TariffSage(tariff_files) # Create an instance of the TariffSage

    while True:
        user_query = input("Consult The Tariff Sage (or type 'E'): ") # Prompt the user for a query
        if user_query.lower() == 'E':
            print("The Tariff Sage bids you farewell.Thank you for being a valuable user!")
            break # Exit the loop if the user types 'E'
        guidance = the_sage.consult_the_sage(user_query) # Get the Sage's response to the query
        print(guidance) # Print the Sage's response
        print("-" * 40) # Print a separator line
