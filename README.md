# *Sales Data Processing and Upload to PostgreSQL*

This project automates the process of reading sales data from CSV files, processing them using Python and Pandas, and uploading the data to a PostgreSQL database. The sales data is stored in JSON and CSV formats, and the application also manages database interactions.

## Table of Contents

-    Project Overview
-    Features
-    Installation
-    Configuration
-    Usage
-    File Structure
-    License

## Project Overview

The application reads sales data from a specified directory, processes the data using Pandas, and inserts it into a PostgreSQL database. The directory contains multiple CSV files with sales transactions. The project is designed to automate the flow of data from files to a database, with unique document IDs for each transaction and random discounts applied to simulate sales scenarios.

# Features

-    **CSV File Parsing**: Reads multiple sales data files from a directory based on filename patterns.
-    **Data Processing**: Uses Pandas to read, process, and structure the sales data.
-    **PostgreSQL Integration**: Uploads the processed data into a PostgreSQL database.
-    **Configurable Settings**: Path to sales data and database connection details are configurable via an INI file.
-    **Customizable Discounts**: Random discounts are applied to the sales data during processing.

## Installation
1. **Clone the Repository**:
```
git clone https://github.com/EdvardFarrow/sales_data_processor.git
cd sales_data_processor
```
2. **Install Dependencies**: Ensure you have Python 3.x installed. Install the required Python packages using *pip*:
```
pip install -r requirements.txt
```
The main dependencies include:

-    pandas
-    psycopg2
-    configparser

3. **Set Up PostgreSQL**: Make sure you have a running PostgreSQL database and have created the appropriate schema:
```
   CREATE TABLE public.sales (
	doc_id varchar NULL,
	category varchar NULL,
	item varchar NULL,
	amount int4 NULL,
	price float4 NULL,
	discount int4 NULL,
	total float4 NULL,
	CONSTRAINT sales_unique UNIQUE (doc_id, category, item, amount, price, discount, total)
);
```
## Configuration

Before running the application, you need to configure the paths and database settings in the config.ini file.

1. **Create a *config.ini* file** in the root of your project (if it doesn't already exist):
```
    [Paths]
    directory = .
    sales_path_pattern = ^\d{1,2}_\d{1,2}\.csv$

    [Database]
    host = localhost
    database = your_database_name
    user = your_db_username
    password = your_db_password
```
- **Paths**: Set the directory where your CSV files are stored and the regex pattern that matches your sales files.
- **Database**: Provide your PostgreSQL connection details (host, database name, user, and password).

## Usage

To run the project:

1.**Generate Sales Data**: To generate the sales data manually, run the following command:
```
python3 /path_to/generate-sales-data.py
```
2.**Upload Data to Database**: After generating the sales data, you can upload it to the PostgreSQL database by executing:
```
python3 /path_to/run.py
```

### Automated Execution with Cron

To automate the process of generating and uploading sales data, you can set up *cron* jobs. The following configurations are recommended:
1. **Generate Fake Sales Data**: This script runs every hour from 9 AM to 10 PM, Monday to Saturday:
```
 0 9-22 * * 1-6 <which python command> </path_to/generate_sales_data.py command>
```
2. **Upload Data to Database**: This script uploads the generated sales data to the PostgreSQL database every day at 10:01 PM, Monday to Saturday:    
```
1 22 * * 1-6 <which python command> </path_to/run.py command>
```
### Setting up Cron Jobs
1. **Open the crontab for editing**:
```
crontab -e
```
2. **Add the above cron job entries** to the file and save it. This will schedule your scripts to run automatically according to the specified times.

**Generated Document IDs**: Each sales transaction gets a unique doc_id in the format CHK-YYYYMMDD-XXXX, where XXXX is a random alphanumeric string.

**Debugging**: The script prints file paths and queries for debugging purposes. Make sure to check the console for any errors.

## File Structure

**The project is structured as follows**:
```
sales-data-processor/
│
├── config.ini                       # Configuration file for paths and database credentials
├── generate-sales-data.py           # Script for generate data
├── run.py                           # Script for upload a data in database
├── pgdb.py                          # Class handling PostgreSQL database connection and queries
├── home_goods_store.json            # Sample JSON file containing product data for sales simulation
├── example_of_generated_data.png    # Screenshot of generated data
├── example_of_uploaded_data.png     # Screenshot of uploaded data 
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation (this file)
```
- generate-sales-data.py: The script that generates fake sales data and saves it as a CSV file for further processing.
- run.py: The script that uploads the generated sales data from the CSV file to the PostgreSQL database.
- pgdb.py: Contains the PGDatabase class for handling PostgreSQL connections.
- home_goods_store.json: Stores product categories and prices, used to simulate sales data.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.
