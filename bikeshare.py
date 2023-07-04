import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
    
            city = input ("\n please choose a city from this list:\n"
                    "chicago"
                    "new york city" "washington").lower()
                  
            if city not in CITY_DATA:
                  print("undifined city , please choose from chicago ,new york city,washington ")
                  
                  
            else:
                break
                    
                  
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
     month = input('please enter the name of month that you want or write all to see the full data').lower()
     months = ('january', 'february', 'march', 'april', 'june', 'july')
    
     if 'month' != 'all' and month not in months:
                 print('please write the correct name of month or write all')
                  
     else:
         break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = ('please enter the name of day that you want or enter all to see full data')            
      days = ( 'sunday','monday','tuesday','wednesday','thursday', 'friday', 'saturday')
      if day not in days and day != 'all':
                  print('please enter a correct name of days or write all')
                  
      else:
          break
                  

print('-'*40)



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

df = pd.read_csv(CITY_DATA)

df['Start_Time'] = pd.to_datatime(df['Start Time'])

df['month'] = df['Start Time'].dt.month

df['day_of_week'] = df['Start Time'].dt.day_name()


if 'month' != 'all' :
    months = ['january', 'february', 'march', 'april', 'june', 'july']
    month = months.index('month') + 1   
    
    df = df['month'] ==  'month'
    
if 'day' != 'all' :    
    df = df['day_of_week'] ==  'day'


def display_raw_data(df):
    
 i = 0

 answer = input('Do you like to see the first 5 raws od data? yes or no')
 pd.set_option('display.max_colomns', None)
while True:
    if 'answer' == 'no':
        break
i = 0
   
print(df[i:i+5])

answer = input('do you want more 5 raws?')
i += 5
        
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

    # TO DO: display the most common month
                  
most_common_month = df['month'].mode()[0]
print('the most common month is:' , most_common_month)

    # TO DO: display the most common day of week
most_common_day = df['day of week'].mode()[0]
print('the most common day is' , most_common_day)

    # TO DO: display the most common start hour

filename = 'chicago.csv'

df = pd.read_csv(filename)

df['Start Time'] = pd.to_datetime(df['Start Time'])

df['hour'] = df['Start Time'].dt.hour

popular_hour = df['hour'].mode()[0]

print('Most Popular Start Hour:', popular_hour)

print("\nThis took %s seconds." % (time.time() - start_time))

print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()

    # TO DO: display most commonly used start station
common_start_satation = df ['Start Station'].mode()
print('the most commonly used start station is:' ,  common_start_satation)


    # TO DO: display most commonly used end station
common_end_satation = df['End station'].mode()[0]
print('the  most commonly used end station is:' ,  common_end_satation)


    # TO DO: display most frequent combination of start station and end station trip
most_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
print("the most frequent combination of start station and end station trip is : {}, {}".format(most_start_end_station[0], most_start_end_station[1]))


print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
start_time = time.time()

    # TO DO: display total travel time
total_time = ['Trip Duration'].sum()
print( 'the total travel time is' , total_time/3600 , 'hours')

    # TO DO: display mean travel time
mean_time = df['Trip Duration'].mean()
print( 'the average travel time is' , mean_time/3600 , 'hours')
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
start_time = time.time()

    # TO DO: Display counts of user types

filename = 'chicago.csv'

df = pd.read_csv(filename)

user_types = df['User Type'].value_counts()

print(user_types)


 # TO DO: Display counts of gender
if 'Gender' in df:
    print('counts of gender:' , df['Gender'].value_counts())
          
 # TO DO: Display earliest, most recent, and most common year of birth
if 'Birth Year' in df:
                 earliest_year = int(df['Birth Year'].min())
                 most_recent = int(df['Birth Year'].max())
                 most_common = int(df['Birth Year'].mode()) 
                                          
                 print('the earliest year of birth is', earliest_year) 
                 print('the most recent year of birth is', most_recent)                  
                 print('the most common year of birth is', most_common)                  


print("\nThis took %s seconds." % (time.time() - 'start_time'))
print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

