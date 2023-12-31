
# Reddit WallStreetBets Stock Prediction App

## Overview

This project aims to build a data pipeline that automatically collects data from the Reddit WallStreetBets API and stores it in a MySQL database. The collected data will be used to develop a machine learning model to predict stock prices, which will be integrated into a web app. This project aligns well with my background in data engineering and my passion for leveraging technology to make a real-world impact.

## Features

- Automated data collection from the Reddit WallStreetBets API.
- Data storage in a MySQL database.
- (Upcoming) Machine learning model for stock price prediction.
- (Upcoming) Web app built using Django (backend) and React (frontend).
- (Planned) Implementation of Azure automation to streamline data collection and processing tasks.

## Installation

### Requirements

- Python 3.x
- MySQL Server

### Setting Up the Database

1. Install MySQL Server.
2. Create a database and set up the necessary tables. Refer to the `pipeline.py` script for table structure.

### Setting Up the Python Environment

1. Clone the repository:
   ```
   git clone https://github.com/your-github-username/repository-name.git
   ```
2. Navigate to the project directory:
   ```
   cd repository-name
   ```
3. Install the necessary Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Update the MySQL connection details in the `pipeline.py` script with your database information.
2. Run the script to start collecting data:
   ```
   python pipeline.py
   ```

## Future Work

- Develop a machine learning model for predicting stock prices based on the collected data.
- Integrate the prediction model into a web app.
- Build a frontend interface using React to interact with the prediction model.
- Implement Azure automation to facilitate continuous data collection and update processes without duplication.

## Contributing

If you are interested in contributing to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or collaboration opportunities, feel free to reach out to me at (your contact information).

## Acknowledgements

- [Reddit WallStreetBets API](https://tradestie.com/api/v1/apps/reddit)
