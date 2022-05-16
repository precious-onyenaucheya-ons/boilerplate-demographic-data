import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv('adult.data.csv', delimiter = ',')

    # How many of each race are  represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(data[data.sex == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    len_bsc = len(data[data.education == 'Bachelors'])
    len_data = len(data)
    percentage_bachelors = round(len_bsc/len_data *100, 1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education =data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])] 

    # percentage with salary >50K

    no_higherEdu_earning = len(higher_education[higher_education.salary == '>50K'])

    no_lowerEdu_earning = len(lower_education[lower_education.salary == '>50K'])

    higher_education_rich = round(no_higherEdu_earning / len(higher_education) * 100, 1 )
    lower_education_rich = round(no_lowerEdu_earning / len(lower_education) * 100, 1 )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = data['hours-per-week'].min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = data[data['hours-per-week']== min_work_hours]
#min_hours
    
    num_min_workers =min_hours[min_hours['salary'] == '>50K'] 

    rich_percentage = round(len(num_min_workers) /len(min_hours) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_count = data['native-country'].value_counts()
    country_rich_count = data[data['salary'] == '>50K']['native-country'].value_counts()  
    highest_earning_country =  (country_rich_count/ country_count * 100).idxmax()

    highest_earning_country_percentage = round((country_rich_count/ country_count * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India
    indians= data[(data['native-country'] =='India') & (data['salary']=='>50K')]
    occupation_counts = indians['occupation'].value_counts()
    top_IN_occupation = occupation_counts.idxmax()
    top_IN_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
