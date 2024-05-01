# AI Spam Detection 

This project is built off of the sklearn module and trains using a .csv dataset file
The goal of the project is to properly detect spam within a dataset using multiple AI models,
allowing users to identify and train the most effective AI model.

# Dataset

This project requires a csv file with at least the two following fields: "text" and "label_num"
- text: The text that is either spam or ham
- label_num: the label that specifies whether the entry is spam (1) or isn't spam (0)

The default dataset provided within this project is a subset of the dataset found at https://www2.aueb.gr/users/ion/data/enron-spam/ under the Enron1 folder.
It has been iterated over and converted to a csv file by Venkatesh Garnepudi on kaggle: https://www.kaggle.com/datasets/venky73/spam-mails-dataset

# Python Dependencies

This project uses Python and requires the following dependencies:

- flask
- flask-socketio
- pandas
- numpy
- scikit-learn

In order to install any of the required python modules, you may run 
* pip install (moduleName)

# Simple startup

Depending on your operating system, run the associated LaunchProgram file.

- Macbooks: LaunchProgram.sh
- Windows: LaunchProgram.bat
- Linux: LaunchProgram.bash

* Macbook start file has not been tested. If any issues arrise, please try starting the server manually

# Manual startup

To startup the program, move to the Project_FINAL directory and run the server.py file using python
- Python server.py

This will open port 5000 upon the computer, in which you can reach via a web browser at url http://localhost:5000 to control the application.