# *Sales Data Processing and Upload to PostgreSQL*

This project automates the process of reading sales data from CSV files, processing them using Python and Pandas, and uploading the data to a PostgreSQL database. The sales data is stored in JSON and CSV formats, and the application also manages database interactions.
Table of Contents

    Project Overview
    Features
    Installation
    Configuration
    Usage
    File Structure
    License

Project Overview

The application reads sales data from a specified directory, processes the data using Pandas, and inserts it into a PostgreSQL database. The directory contains multiple CSV files with sales transactions. The project is designed to automate the flow of data from files to a database, with unique document IDs for each transaction and random discounts applied to simulate sales scenarios.
Features

    CSV File Parsing: Reads multiple sales data files from a directory based on filename patterns.
    Data Processing: Uses Pandas to read, process, and structure the sales data.
    PostgreSQL Integration: Uploads the processed data into a PostgreSQL database.
    Configurable Settings: Path to sales data and database connection details are configurable via an INI file.
    Customizable Discounts: Random discounts are applied to the sales data during processing.

Installation

    Clone the Repository:

    bash

git clone https://github.com/your-username/sales-data-processor.git
cd sales-data-processor

Install Dependencies: Ensure you have Python 3.x installed. Install the required Python packages using pip:

bash

pip install -r requirements.txt

The main dependencies include:

    pandas
    psycopg2
    configparser

Set Up PostgreSQL: Make sure you have a running PostgreSQL database and have created the appropriate schema:

sql

    CREATE TABLE sales (
        doc_id VARCHAR(50),
        category VARCHAR(100),
        item VARCHAR(100),
        amount INT,
        price DECIMAL,
        discount DECIMAL,
        total DECIMAL
    );

Configuration

Before running the application, you need to configure the paths and database settings in the config.ini file.

    Create a config.ini file in the root of your project (if it doesn't already exist):

    ini

    [Paths]
    directory = /path/to/sales/csv/files
    sales_path_pattern = sales_.*\.csv

    [Database]
    host = localhost
    database = your_database_name
    user = your_db_username
    password = your_db_password

        Paths: Set the directory where your CSV files are stored and the regex pattern that matches your sales files.
        Database: Provide your PostgreSQL connection details (host, database name, user, and password).

Usage

To run the project:

    Process and Upload Sales Data:

    bash

    python main.py

    This will:
        Read all CSV files matching the sales_path_pattern in the specified directory.
        Process the sales data into Pandas DataFrames.
        Insert the processed sales data into your PostgreSQL database.

    Generated Document IDs: Each sales transaction gets a unique doc_id in the format CHK-YYYYMMDD-XXXX, where XXXX is a random alphanumeric string.

    Debugging: The script prints file paths and queries for debugging purposes. Make sure to check the console for any errors.

File Structure

The project is structured as follows:

bash

sales-data-processor/
│
├── config.ini                 # Configuration file for paths and database credentials
├── main.py                    # Main script to run the sales data processing and upload
├── pgdb.py                    # Class handling PostgreSQL database connection and queries
├── home_goods_store.json       # Sample JSON file containing product data for sales simulation
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation (this file)

    main.py: The main entry point that processes the sales files and uploads them to the database.
    pgdb.py: Contains the PGDatabase class for handling PostgreSQL connections.
    home_goods_store.json: Stores product categories and prices, used to simulate sales data.

License

This project is licensed under the MIT License. See the LICENSE file for details.