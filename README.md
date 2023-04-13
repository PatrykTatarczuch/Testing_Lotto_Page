Web application for Lotto

This repository contains the source code of a web application that simulates playing the lottery.

The application allows users to choose six numbers between 1 and 49, and any use of numbers outside of this range will be blocked. It was built using the Flask framework, as well as HTML and Python.

Installation and usage:

Step 1:
To run the web application, you need to have Python 3, Visual Studio Code, and the version control system "Git" installed on your computer.

Step 2:
After installing all necessary applications, open the terminal in Visual Studio Code and type:
"git clone https://github.com/PatrykTatarczuch/Testing_Lotto_Page.git"
This will clone all files from my repository to your Visual Studio Code.

Step 3:
I have placed all other required packages in the requirements.txt file. To install them, type the following command in the terminal:
"pip install -r requirements.txt"

Step 4:
After installing the required packages, you can run the application by running the "app.py" script. This will start the server, and the web application can be opened by entering the generated address: http://localhost:5000 or by clicking on it in the terminal.

Step5:
After starting the server, create a new environment by adding a new terminal. It is important that the server is not stopped while you work. The tests are located in the "tests" folder and can be run by navigating to the main project directory and running the following command in a new terminal:
"pytest --html=reports.html"
This command will generate an HTML report with the test results in the "reports.html" file. You can open the HTML file by clicking on the link generated in the test report.

Acknowledgments:

The application was built by Patryk Tatarczuch as a personal project. Some scripts used in the index.html file were generated using the ChatGPT4 language model. If you have any questions or suggestions, please contact me at patryktatarczuch22@gmail.com
