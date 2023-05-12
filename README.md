Student Rank Sorter Web Script
==============================

This is a web script that sorts the students' ranks using Python and web scraping.

How it works
------------
The script scrapes the website http://app2.helwan.edu.eg for students' grades. It loops over the range of students' IDs from 61392 to 61756 and extracts each student's name and total grade. It then stores the data in a list of tuples, where each tuple contains the student's name and their total grade. Finally, the script sorts the list in descending order based on the grades and writes the sorted list to a text file called Comm.txt.

Requirements
------------
- Python (tested with version 3.9)
- Beautiful Soup 4 (bs4) library
- Requests library

How to use
----------
1. Clone the repository.
2. Install the required libraries by running `pip install -r requirements.txt` in your terminal.
3. Run the script by running `python sort_students.py`.
4. The sorted list will be written to Comm.txt.

Contributing
------------
If you want to contribute to this project, you can:
- Submit bug reports or feature requests in the issues section.
- Fork the repository and make changes.
- Submit pull requests.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.
