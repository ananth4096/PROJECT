import time
import pandas as pd
import numpy as np
import sys

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
    print("\nHello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Choose the name of the city ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Choose the city name in between 'chicago', 'new york city' OR 'washington': ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Choose Month in january, february, march, april, may, june, all\n").lower()
    while month not in months:
       print('Require Correct Data')
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose the day in sunday, monday, tuesday, wednesday, thursday, friday, saturday, all\n").lower()
    if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
         print('Require Correct Data')

            
        

    print('-'*40)
    return city, month, day


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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #Extract month and day of week from starttime column to database
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        
    df = df[df['month'] == month]
        
    if day != 'all':
      df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(" The Most Common Month was", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The Most Common Day of Week was", df['day_of_week'].mode()[0])
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(" The most common hour was", df['hour'].mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station was {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station was {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+ ',' + df['End Station']
    print('The most common route is {}'.format(df['route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600.0
    print('Total Travel Time in hours:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/3600.0
    print('Mean Travel Time in hours :',mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
         


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
        print('user_type')
    except KeyError:
        print('no data available for washington city.')
        sys.exit(1)

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('user_gender')
    except KeyError:
        print('no data available for washington city.')
        sys.exit(1)
          


    # TO DO: Display earliest, most recent, and most common year of birth
    print('The most recent year of birth is :',int(df['Birth Year'].max()))
    print('The earliest year of birth is :',int(df['Birth Year'].min()))
    print('The most common year of birth is :',int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    print('Please enter yes to see the row data ,otherwise enter no to skip ')
    i=0
    while (input() != 'no'):
        i += 5
        print(df.head(i))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
