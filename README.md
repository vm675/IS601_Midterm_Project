# **Midterm Project: Dosa Orders Processing**  




This project processes restaurant orders from example_orders.json and extracts customer and item information into structured JSON files. The customers.py script reads the input JSON, extracts phone numbers and names, and saves them in customers.json. The items.py script processes the orders to extract item names, prices, and the number of times each item has been ordered, saving the results in items.json. Both scripts ensure that duplicate customer entries are not repeated and that item orders are correctly counted. After execution, running python customers.py will generate customers.json, and running python items.py will generate items.json, confirming success with a terminal message. These output files allow for better order tracking and analysis for the restaurant. To verify the results, users can check the generated JSON files using the cat customers.json and cat items.json commands.

Installation & Setup:
Ensure Python 3.3+ and Git are installed. Clone the repository using git clone <https://github.com/vm675/IS601_Midterm_Project/blob/main/README.md>, navigate to the project folder with cd midterm_project, and ensure all files are in the same directory. Since the project uses only built-in Python libraries, no additional installations are required.







