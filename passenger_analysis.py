import pandas as pd
from datetime import datetime

def find_loyalty_members(df, travel_class): # a & b are swapped in the assignment lol. calculate_average_age wants loyalty members, find_loyalty_members wants to calculate age.
    loyals = df[(df['LoyaltyMember'] == True) & (df['TravelClass'] == travel_class)]['Name'].tolist()
    return loyals

def calculate_average_age(df, travel_class):
  filtration = df[df['TravelClass'] == travel_class].copy()
  filtration['Birthdate'] = pd.to_datetime(filtration['Birthdate'])
  present = datetime.today()
  filtration['Age'] = present.year - filtration['Birthdate'].dt.year
  final_average = filtration['Age'].mean()
  return round(final_average)

def get_class_statistics(df):
    travel_classes = df['TravelClass'].unique()
    stats = {}
    
    for travel_class in travel_classes:
        average_age = calculate_average_age(df, travel_class)
        loyalty_members = len(find_loyalty_members(df, travel_class))
        
        stats[travel_class] = {
            'Average Age': round(average_age),  # Ensure average age is rounded
            'Loyalty Members': loyalty_members
        }
    
    return stats