import pandas as pd
import phonenumbers
from phonenumbers import is_valid_number, parse
import pycountry
import re
class DataCleaning:
    """
    A class for cleaning data from various sources.
    """

    def __init__(self):
        pass  # The constructor method is empty, as no initialization is needed

    def validate_phone(self, phone_number):
        """
        Helper function to validate the phone number format using regex.

        Args:
            phone_number (str): The phone number to be validated.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        pattern = r'^[^a-zA-Z]*\d{6,}[^a-zA-Z]*$'
        
        if re.match(pattern, phone_number):
            return True
        else:
            return False

        


    # Task 3 step 6
    def clean_user_data(self, df):  # Define a method to clean the user data DataFrame (Task 3, Step 6)
        """
        Clean the user data DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame containing user data to be cleaned.

        Returns:
            pandas.DataFrame: The cleaned user data DataFrame.
        """

        # Convert date_of_birth column to datetime format
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], infer_datetime_format=True,errors='coerce')

        # Drop rows with remaining invalid dates
        df = df.dropna(subset=['date_of_birth'])
        
        # Validating country code
        df['country_code'] = df.apply(lambda x: x.country_code if pycountry.countries.get(alpha_2=x.country_code) else None, axis='columns')
        
        # we check if we are able to look it  up using pycountry, if so then the country_code is valid. else we change it to a null value.

        # Dropping rows with invalid country code
        df = df.dropna(subset=['country_code'])
        
        # Validating phone numbers
        df['phone_number'] = df['phone_number'].apply(lambda x: x if re.match(r'^[^a-zA-Z]*\d{6,}[^a-zA-Z]*$', str(x)) else None)

        # Dropping rows with invalid phone number
        df = df.dropna(subset=['phone_number'])

        return df  # Return the cleaned user data DataFrame
