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
    # Get user input for city (chicago, new york city, washington).
    city = input('Please type a city.  The options are "Chicago", "New York City", and "Washington".\n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('That wasn\'t a city I recognize. The options are "Chicago", "New York City", and "Washington".  Please make a valid selection.\n').lower()
        
    # Get user input for month (all, january, february, ... , june).
    month = input('Please type a month.  You can choose "January", "February", "March", "April", "May", "June", or "All" (to see all months).\n').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('That wasn\'t a month I recognize. The options are  "January", "February", "March", "April", "May", "June", or "All".  Please make a selection.\n').lower()
        
    # Get user input for day of week (all, monday, tuesday, ... sunday).
    day = input('Please type a day of the week.  For example, "Monday", "Tuesday", etc. or "All" (to see all days).\n').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('That wasn\'t a day of the week I recognize.  The options are "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", or "All".  Please make a selection.\n').lower()
        
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
    df = pd.read_csv(CITY_DATA[city])
    # Add a start time column.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
<<<<<<< HEAD
    # Make a month column.
    df['month'] = df['Start Time'].dt.month
    # Make a day of week column.
=======
    # Make month and day of week columns.
    df['month'] = df['Start Time'].dt.month
>>>>>>> a8106c912dcd2a933580708d1af1f53c683e3a14
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filter by month.
    if month != 'all':
<<<<<<< HEAD
	# These are all of the months we expect to see in our data set.
=======
>>>>>>> a8106c912dcd2a933580708d1af1f53c683e3a14
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week.
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month.
    popular_month = df['month'].mode()[0] - 1
    popular_month = ['January', 'February', 'March', 'April', 'May', 'June'][popular_month]
    print('Most Popular Month:', popular_month)


    # Display the most common day of week.
    popular_dow = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_dow)


    # Display the most common start hour.
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station.
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # Display most commonly used end station.
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # Display most frequent combination of start station and end station trip.
    df['Trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('Most Popular Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time.
    print('Total Travel Time:', df['Trip Duration'].sum())
    

    # Display mean travel time.
    print('Mean Travel Time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types.
    print(df.groupby(['User Type']).count()[['Trip']])

    # Display counts of gender.
    try:
        print('\n',df.groupby(['Gender']).count()[['Trip']])
    except:
        print('\nNo gender data available for this city.')

    # Display earliest, most recent, and most common year of birth.
    try:
        print('\nMost Recent Birth Year:', df['Birth Year'].max())
        print('Earliest Birth Year:', df['Birth Year'].min())
        print('Most Common Birth Year:', df['Birth Year'].mode()[0])
    except:
        print('\nNo birth year data available for this city.')
    

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
        
        # Ask if the user wants to see raw data.
        df = pd.read_csv(CITY_DATA[city])
<<<<<<< HEAD
	# these indices set up an interval of records
=======
>>>>>>> a8106c912dcd2a933580708d1af1f53c683e3a14
        i,j=0,5
        view_raw = input('Would you like to see five records of raw data?  Please indicate "Yes" or "No".\n').lower()
        while view_raw not in ['yes', 'no']:
            view_raw = input('That wasn\'t an option I recognize.  Please type "Yes" or "No" to indicate if you\'d like to review five records of raw data.\n').lower()
        
        while view_raw == 'yes':
            print(df.iloc[i:j])
            view_raw = input('Would you like to see five more records of raw data?  Please indicate "Yes" or "No".\n').lower()
            while view_raw not in ['yes', 'no']:
                view_raw = input('That wasn\'t an option I recognize.  Please type "Yes" or "No" to indicate if you\'d like to review five records of raw data.\n').lower()
<<<<<<< HEAD
	# this increments the interval of records to view
=======
>>>>>>> a8106c912dcd2a933580708d1af1f53c683e3a14
            i += 5
            j += 5
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        


if __name__ == "__main__":
	main()
