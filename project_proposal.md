# Project Proposal

---

## 1. The Big Idea

My  project, the **Amazon Spending Tracker**, aims to help users better understand their Amazon purchasing habits by analyzing their order history data. Amazon allows users to download an order report as a CSV file, but the raw data is difficult to interpret without additional tools. This project turns that spreadsheet into clear insights about spending patterns, categories, and trend monthly or in whatever time format the designer may feel is most adequate. 

The central goal  is to build a Python program that loads the user’s Amazon order history CSV and extracts meaningful information such as:

1.  Total spending  
2.  Spending by category  
3. Monthly spending trends  
4.  Number of items purchased 
5.  Top spending categories  

Most people don’t realize how much they spend on Amazon each month or what categories contribute the most to their expenses on the website in a monthly fashion.This tool answers those questions in an organized, accessible way.

**Minimum Viable Product (MVP):**

- Load the CSV file  
- Clean and parse the relevant fields (order date, item total, order category, etc.)  
- Compute total spending  
- Break down spending by category  
- Summarize monthly spending  
- Display all results clearly in the console  

**Stretch Goals:**

- Generate data visualizations (monthly spending chart, category bar graph)  
- Export a PDF or HTML report  
- Detect subscription-like recurring purchases  
- Add a simple GUI for easier use  (probably with the use of Javascript for interactivity and CSS for styling)



---

## 2. Learning Objectives

**Individual Goals**

- Practice real data ingestion and cleaning in Python  
- Apply software design principles through modular architecture  
- Improve collaborative workflow using GitHub  
- Become comfortable with parsing CSV and handling messy data  
- Learn how to build reusable Python modules and functions  
- Explore data visualization or GUI programming  

---

## 3. Implementation Plan

I want to plan to build the application in several components:

- **Data Import Module:** Load and parse CSV files exported from Amazon  
- **Cleaning & Categorization Module:** Standardize data fields, handle missing values, assign spending categories  
- **Analytics Module:** Compute summaries (totals, averages, category spending, monthly trends)  
- **CLI Interface:** Provide menus for uploading data, viewing summaries, and exporting results  

**Research Areas:**

- Best practices for data cleaning  
- Matplotlib for charts 
- Tkinter basics for GUIs
- File export formats (CSV, PDF)  

---

## 4. Project Schedule

- **Week 1:** Finalize idea, set up repository, define data structure and modules  
- **Week 2:** Implement data import and cleaning functions  
- **Week 3:** Build core analytics and CLI display  
- **Week 4:** Begin stretch goals (charts, export features)  
- **Week 5:** Polish UI/UX, finalize documentation, prepare submission  

---

## 5. Collaboration Plan
Since I will be working individually I will find time to reflect and go over the project weekly schedule on a weekly basis to plan goals. Tasks will be divided by module, but complex parts (like categorization or visualizations) will be tackled through programming meeting sessions since I will still be meeting with friend like Daniel so I can show him my work and he can provide suggestions for me on what to incorporate or change. 

**Tools and Methods:**

- GitHub Projects for task tracking  
- Weekly sprints inspired by Agile methodology  
- Pull requests for code review before merging  

---

## 6. Risks and Limitations

- Amazon exports can be inconsistent depending on region and account settings so the accuracy may vary from person to person. 
- Data cleaning may require significant effort  
- Visualizations or GUI may take longer than expected since I will be using Javascript,HTML,CSS and Python ill probably have to weight out functionalality over appearance in some cases.  
- CSV files may be large if a user has many years of purchases, so there could be a stop point within the program like it can only go back 1-2 years or only be put in months.   

---

## 7. Additional Course Content

Topics that would be beneficial:

- Advanced file handling and exceptions  
- Data cleaning patterns  
- Debugging and modular design  
-  visualization libraries and GUI tools

---
