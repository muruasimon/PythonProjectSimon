import requests
import json
import snowflake.connector

def GetDataApi():
    response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
    data = response_API.json()  # Parse JSON directly into a dictionary
    return data

def save_to_snowflake(data):
    # Establish connection to Snowflake
    conn = snowflake.connector.connect(
        user='jccharaf',
        password='BEBE.flor.12',
        account='APIHRLR-ZG30772',
        warehouse='COMPUTE_WH',
        database='WEATHER',
        schema='PUBLIC'
    )

    # Create a cursor object
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS covid_data (
            state VARCHAR,
            district VARCHAR,
            confirmed INT,
            active INT,
            recovered INT,
            deceased INT
        )
    """)

    # Insert data into the Snowflake table
    for state, state_data in data.items():
        for district, district_data in state_data['districtData'].items():
            cur.execute("""
                INSERT INTO covid_data (state, district, confirmed, active, recovered, deceased)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                state,
                district,
                district_data.get('confirmed', 0),
                district_data.get('active', 0),
                district_data.get('recovered', 0),
                district_data.get('deceased', 0)
            ))
    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

# Main function to fetch data and save to Snowflake
def main():
    data = GetDataApi()
    save_to_snowflake(data)

if __name__ == "__main__":
    main()
