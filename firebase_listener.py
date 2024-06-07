from utils import db
import pandas as pd
import time

def upload_to_firebase():
    # Read the Excel file
    try:
        xls = pd.ExcelFile('../../Data/VisaClimateTechData.xlsx')
        df1 = pd.read_excel(xls, '2_Card data')
        df2 = pd.read_excel(xls, '3_Open banking data')

        # Loop through DataFrame and upload data to Firebase Realtime Database
        # for index, row in df1.iterrows():
        #     data = row.to_dict()
        #     db.child("card_data").push(data)
        
        # Convert datetime columns to string format
        for df in [df1, df2]:
            for column in df.columns:
                if pd.api.types.is_datetime64_any_dtype(df[column]):
                    df[column] = df[column].astype(str)

        # Convert DataFrame to list of dictionaries
        data_list1 = df1.to_dict(orient='records')
        data_list2 = df2.to_dict(orient='records')

        # Push data to Firebase
        for record in data_list1:
            db.child('card_data').push(record)
            time.sleep(0.1)  # Small delay to prevent overwhelming the database

        for record in data_list2:
            db.child('open_banking_data').push(record)
            time.sleep(0.1)  # Small delay to prevent overwhelming the database

        print("Data uploaded successfully")

    except Exception as e:
        print(f"An error occured: {e}")

upload_to_firebase()
