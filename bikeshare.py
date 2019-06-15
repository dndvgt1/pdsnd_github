import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#---------------------------------------------------------------------------------------------------------------------------
def f_get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day   - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\n')
    print('---------------------------------------------')
    print('Hello! Let\'s explore some US bikeshare data!')
    print('---------------------------------------------')
    print('\n')
    
    print('Please select data filters to apply --')
    
    # TO DO: get user input for city (chicago, new york city, washington)
    city_filter = 0
    while city_filter not in [1, 2, 3]:        
        city_filter = int(input("CITY (choose corresponding number):  \
               \n[1] Chicago  \n[2] New York City  \n[3] Washington D.C. \n"))
        
        if city_filter not in [1, 2, 3]:
            print('\n[Error.  Choose a valid number.]')

    if city_filter == 1:
        city = 'chicago'
    elif city_filter == 2:
        city = 'new york city'
    elif city_filter == 3:
        city = 'washington'           
            
               
    # TO DO: get user input for month (all, january, february, ... , june)
    month_filter = -1
    while month_filter not in [0, 1, 2, 3, 4, 5, 6]:
        month_filter = int(input("MONTH (choose corresponding number):  \
                \n[0] All months available  \n[1] January  \n[2] February  \n[3] March  \
                \n[4] April  \n[5] May  \n[6] June \n"))

        if month_filter not in [0, 1, 2, 3, 4, 5, 6]:
            print('\n[Error.  Choose a valid number.]')                          

    if month_filter == 0:
        month = 'all'
    elif month_filter == 1:
        month = 'january'
    elif month_filter == 2:
        month = 'february'
    elif month_filter == 3:
        month = 'march'
    elif month_filter == 4:
        month = 'april'
    elif month_filter == 5:
        month = 'may'
    elif month_filter == 6:
        month = 'june'        
        
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_filter = -1
    while day_filter not in [0, 1, 2, 3, 4, 5, 6, 7]:
        day_filter = int(input("DAY (choose corresponding number):  \
                \n[0] All days  \n[1] Sunday  \n[2] Monday  \n[3] Tuesday  \
                \n[4] Wednesday  \n[5] Thursday  \n[6] Friday  \n[7] Saturday \n"))

        if day_filter not in [0, 1, 2, 3, 4, 5, 6, 7]:
            print('\n[Error.  Choose a valid number.]')  

    if day_filter == 0:
        day = 'all'
    elif day_filter == 1:
        day = 'sunday'
    elif day_filter == 2:
        day = 'monday'
    elif day_filter == 3:
        day = 'tuesday'
    elif day_filter == 4:
        day = 'wednesday'
    elif day_filter == 5:
        day = 'thursday'
    elif day_filter == 6:
        day = 'friday'        
    elif day_filter == 7:
        day = 'saturday'   

    print('\n')
    print('-'*70)
    
    return city, month, day

    
#---------------------------------------------------------------------------------------------------------------------------
def f_load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day   - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 

    return df


#---------------------------------------------------------------------------------------------------------------------------
def f_time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    
    print('\n')
    print('-'*70)
    print('Calculating The Most Frequent Times of Travel...')
    print('-'*70)
    start_time = time.time()

    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    # TO DO: display the most common month
    # extract month from the Start Time column to create a [month] column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most popular Month:  ', popular_month)

    
    # TO DO: display the most common day of week
    # extract day of week from the Start Time column to create a [day_of_week] column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # find the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most popular Day Of Week:  ', popular_day_of_week)

    
    # TO DO: display the most common start hour   
    # extract hour from the Start Time column to create an [hour] column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular Start Hour:  ', popular_hour)
    
    print('\n')
    print("This took %s seconds." % (time.time() - start_time))


#---------------------------------------------------------------------------------------------------------------------------
def f_station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """

    print('\n')
    print('-'*70)
    print('Calculating The Most Popular Stations and Trip...')
    print('-'*70)
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("Most commonly used [Start Station]:  ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("Most commonly used [End Station]:  ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_stations = df[["Start Station", "End Station"]].mode()
    print("Most frequent combination of [Start Station]-[End Station]:\n", most_common_start_end_stations)
    
    print('\n')
    print("This took %s seconds." % (time.time() - start_time))


#---------------------------------------------------------------------------------------------------------------------------
def f_trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """

    print('\n')
    print('-'*70)
    print('Calculating Trip Duration...')
    print('-'*70)
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time (in hours):  ', df['Trip Duration'].sum()/60/60)

    # TO DO: display mean travel time
    print('Mean Travel Time (in minutes):  ', df['Trip Duration'].mean()/60)

    print('\n')
    print("This took %s seconds." % (time.time() - start_time))


#---------------------------------------------------------------------------------------------------------------------------
def f_user_stats(df):
    """
    Displays statistics on bikeshare users.
    """

    print('\n')
    print('-'*70)
    print('Calculating User Stats...')
    print('-'*70)
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)
    print('\n')

    
    # TO DO: Display counts of gender
    # print value counts for gender    
    try:
        genders = df['Gender'].value_counts()
        print(genders)
    except(KeyError):
        # this because of missing Gender column for Washington D.C.
        print('[No Gender data available for Washington D.C.]')

        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\n')
        print('Earliest Birth Year   :  ', int(df['Birth Year'].min()))
        print('Most Recent Birth Year:  ', int(df['Birth Year'].max()))
        print('Most Common Birth Year:  ', int(df['Birth Year'].mode()))
    except(KeyError):
        # this because of missing Birth Year column for Washington D.C.
        print('[No Birth Year data available for Washington D.C.]')
    
    print('\n')
    print("This took %s seconds." % (time.time() - start_time))
    

#---------------------------------------------------------------------------------------------------------------------------
# placeholder refactor module 1
# def f_module_1


#---------------------------------------------------------------------------------------------------------------------------
# placeholder refactor module 2   
# def f_module_2 


#---------------------------------------------------------------------------------------------------------------------------
def main():
   
    while True:
        city, month, day = f_get_filters()
        
        print('Data filters to apply:')
        print('city  - ', city)
        print('month - ', month)
        print('day   - ', day)
        
        df = f_load_data(city, month, day)

        f_time_stats(df)
        f_station_stats(df)
        f_trip_duration_stats(df)        
        f_user_stats(df)
        
        print('\n')
        print('-'*70)
        restart = input('\nWould you like to restart? Enter [yes] or [no].\n')
        if restart.lower() != 'yes':
            break

            
#---------------------------------------------------------------------------------------------------------------------------            
if __name__ == "__main__":
	main()
  
