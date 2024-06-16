import pandas as pd
from passenger_analysis import calculate_average_age, find_loyalty_members, get_class_statistics
import matplotlib as plt
import plotly.express as px
import plotly.io as pio
import seaborn as sns

def load_data(input):
    df = pd.read_csv(input)
    return df

load_data('passengers.csv')

def clean_data(df):
    while 'NaN' in df:
      if df.isnull() != 0:
        df.fillna(method='ffill', inplace=True)
        print(df.loc)
      else:
        print("No missing data found")
    res = df.dtypes
    series_valid = ['int64',object,object,object,bool,object]
    if (res != series_valid).any():
        indices = (res != series_valid).index.tolist()
        raise TypeError("Some columns have incorrect type: {0}".format(indices)) 
        # kudos to this Stack Overflow thread for the assist because the way this part is worded in the assignment is *very* vague: https://stackoverflow.com/questions/50853561/what-is-the-best-way-to-check-correct-dtypes-in-a-pandas-dataframe-as-part-of-te

clean_data('passengers.csv')

print(find_loyalty_members(load_data('passengers.csv'), 'ECONOMY'))
print(find_loyalty_members(load_data('passengers.csv'), 'BUSINESS'))
print(find_loyalty_members(load_data('passengers.csv'), 'FIRST_CLASS'))

print(calculate_average_age(load_data('passengers.csv'), 'ECONOMY'))
print(calculate_average_age(load_data('passengers.csv'), 'BUSINESS'))
print(calculate_average_age(load_data('passengers.csv'), 'FIRST_CLASS'))

print(get_class_statistics(load_data('passengers.csv')))

def plot_age_distribution(df):
    df['Birthdate'] = pd.to_datetime(df['Birthdate']) # convert the Birthdate column to something usable
    
    # Bulk of the calculations
    present = pd.to_datetime('now')
    df['Age'] = present.year - df['Birthdate'].dt.year
    
    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Passenger Age Distribution | Wesley Flores')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('age_distribution.png')
    plt.show()

plot_age_distribution(load_data('passengers.csv'))

def plot_average_age_by_travel_class(df):
    # MATH
    average_age_by_class = df.groupby('TravelClass')['Birthdate'].apply(lambda x: pd.Timestamp.now().year - x.dt.year.mean()).reset_index()
    average_age_by_class.columns = ['TravelClass', 'AverageAge']
    
    # Plot the chart
    plt.figure(figsize=(10, 6))
    plt.bar(average_age_by_class['TravelClass'], average_age_by_class['AverageAge'], color='lightgreen')
    plt.title('Average Age by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Average Age')
    plt.grid(axis='y')
    plt.savefig('average_age_by_class.png')
    plt.show()

plot_average_age_by_travel_class(load_data('passengers.csv'))

def plot_age_distribution_by_class(df):
    # same old
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    
    # same old
    present = pd.Timestamp.now()
    df['Age'] = present.year - df['Birthdate'].dt.year
    
    # Plot box plot of age distribution by travel class using Plotly
    fig = px.box(df, x='TravelClass', y='Age', points='all', title='Age Distribution by Travel Class')
    fig.update_layout(xaxis_title='Travel Class', yaxis_title='Age')
    fig.write_image('age_distribution_by_class.png') # this kaleido installation taking a MONTH. I blame it for making this assignment late.

def plot_age_vs_loyalty(df):
    # sos
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    
    # sos
    present = pd.Timestamp.now()
    df['Age'] = present.year - df['Birthdate'].dt.year
    
    # Plot scatter plot of age vs. loyalty membership
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='LoyaltyMember', data=df, hue='LoyaltyMember', palette='Set1')
    plt.title('Age vs. Loyalty Membership')
    plt.xlabel('Age')
    plt.ylabel('Loyalty Member')
    plt.grid(True)
    plt.savefig('age_vs_loyalty.png')
    plt.show()

plot_age_vs_loyalty(load_data('passengers.csv')) 