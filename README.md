# dbt Project: Dimensional Modeling and Data Transformation

## Project Overview
This project is built using dbt to implement a dimensional model for data transformation. It covers everything from setting up source models to building fact and dimension tables. Since real data wasn’t available, I generated synthetic data using Python's `Faker` library. The project also includes data quality tests and documentation to ensure everything works as expected.

## Project Structure
Here’s how the project is set up:
- **Sources**: Raw data with freshness tests to make sure the data is up-to-date.
- **Staging Models**: Basic transformations on the raw data (e.g., renaming columns, casting data types).
- **Intermediate Models** (Optional): Extra transformations if needed before the final models.
- **Dimensional Models**: Fact and dimension tables to represent the business logic.
- **Data Tests**: Tests to ensure data integrity (like checking for uniqueness and non-null values).

## Tools Used
- **dbt**: For data transformation and modeling.
- **PostgreSQL**: The database used for this project.
- **Faker (Python)**: To generate synthetic data.

## How to Set Up

### 1. Clone the Repository
First, clone the repo to your local machine:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Set Up Virtual Environment
Create and activate a virtual environment (if it’s not set up already):


3. Install Dependencies
Install dbt-core and the PostgreSQL adapter:

pip install dbt-core dbt-postgres

4. Configure Your dbt Profiles
dbt uses a profiles.yml file to connect to your database. Make sure this file is properly set up.
Place this file in the ~/.dbt/ directory.

5. Run dbt Models
Once everything is set up, you can run the transformations with
dbt run

6. Run Data Tests
Check data quality by running dbt test

7. Generate and Serve Documentation
You can generate and view the documentation locally with the following commands:

dbt docs generate
dbt docs serve

This will open the dbt documentation in your web browser.

Data Quality Tests
This project includes data tests to ensure data integrity:

Not Null: Ensures that critical fields (like id) do not contain null values.
Unique: Verifies that fields meant to be unique (like id) contain no duplicates.
