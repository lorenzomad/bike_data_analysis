#(from tarfile import _Bz2ReadableFileobj
import time
import pandas as pd
import numpy as np


#definition of the dictionaries and lists for the association:
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    invalid = True #variable to check if the input is valid
    while(invalid):
        city = input('What city would you like to explore?\n').lower()

        if(city in list(CITY_DATA.keys())):
            invalid = False
        else:
            print("the input is not valid, please try again")

    # get user input for month (all, january, february, ... , june)
    invalid = True
    while(invalid):
        month = input('On what month do you want to filter? (use all for no filter)\n').lower()

        if(month in months_list or month == 'all'):
            invalid = False
            
        else:
            print("the input is not valid, please try again")
        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    invalid = True

    while(invalid):
        day = input('On what day do you want to filter? (use all for no filter)\n').lower()

        if(day in days_list or day == 'all'):
            invalid = False
        else:
            print("the input is not valid, please try again")

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

   
    
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        month_number = months_list.index(month) + 1
    
        df = df[df['month'] == month_number]

    if day != 'all':
        day_number = days_list.index(day)
        df = df[df["day_of_week"] == day_number]
    print(df)
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    frequent_month = df['month'].mode()[0]
    print("The most frequent month for travels is: \n " + months_list[frequent_month - 1])

    # display the most common day of week
    frequent_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is: \n" + days_list[frequent_day])

    # display the most common start hour
    frequent_hour = df['hour'].mode()[0]
    print("The most frequent hour is: " )
    print(frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    frequent_start_station = df['Start Station'].mode()[0]
    print("The most popular starting station is: \n" + frequent_start_station)

    # display most commonly used end station
    frequent_end_station = df['End Station'].mode()[0]
    print("The most popular end station is: \n" + frequent_end_station)


    # display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + ' and ' + df["End Station"]
    frequent_start_end = df['start_end'].mode()[0]
    print("The most popular combination of starting station and end station is: \n" + frequent_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total cumulative duration of travel is: \n" )
    print(total_travel_time)

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average duration of a trip is: \n" )
    print(average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The users are of these types:\n")
    print(user_types)


    # Display counts of gender
    genders = df["Gender"].value_counts()
    print("the distribution between the genders is:\n ")
    print(genders)


    # Display earliest, most recent, and most common year of birth
    oldest = df['Birth Year'].min()
    youngest = df['Birth Year'].max()
    common_birth = df['Birth Year'].mode()[0]
    print("The oldest person was born in: \n" )
    print(int(oldest))
    print("The youngest person was born in: \n" )
    print(int(youngest))
    print("The most common birth year is: \n" )
    print( int(common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
