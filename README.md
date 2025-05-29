# Reimbursement_Management
This file aims to create an AI agent which will manage the reimbursement related queries which will help hospital/clinic staff for better operability called "The Tariff Sage,". You can ask it questions in plain language, and it will try to find answers in the files which are provided by the user.

# Features

* Reads data from `.csv`, `.json`, `.xls`, and `.xlsx` files.
* Looks for keywords from your questions in the tariff data.
* You type your questions in the computer's text window.

# Installation

1.  **Python:** Make sure you have Python 3 installed on your computer. You can get it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  **Libraries:** Install some extra tools Python needs by opening your computer's command line (terminal on Mac/Linux) and typing this, then pressing Enter:

    ```bash
    pip install pandas openpyxl xlrd fuzzywuzzy python-Levenshtein
    ```

# Usage

1.  *Save Tariff Data:* Make sure your hospital's price lists are saved as `.csv`, `.json`, `.xls`, or `.xlsx` files.

2.  *Edit File Paths:* Open the Python script (the file ending in `.py`, like `tariff_sage.py`) in a simple text program. Find the part near the end that looks like this:

    ```python
    if __name__ == "__main__":
        tariff_files = ['path to excel file1.xlsx',
                        'path to excel file 2.xlsx',
                        'path to excel file 3.xls']
    ```

    Change the words inside the square brackets `[]` to the actual locations of your price list files on your computer. If you have two Excel files, you might list them both here.

3.  *Run the Script:* Open your computer's command line again, go to the folder where you saved the Python script, and run it by typing:

    ```bash
    python tariff_sage.py
    ```

4.  *Ask Questions:* The program will start, and you can type your questions about costs and press Enter.

5.  *Exit:* To stop the program, type `exit` and press Enter.

# Example Questions

* "What is the cost for fixing a knee replacement?"
* "How much does insurance cover for code 10293?"
* "Is the price different for dialysis if you don't stay overnight?"
* "What is the code for Brain Tumours?" 


# Future Scope

* Make the agent understand the meaning of your questions better by enhancing the search.
* Give more decriptive answers and explain why it found a certain result.
