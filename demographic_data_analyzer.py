import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_rows = df.shape[0]
    total_bachelors = df[df["education"] == "Bachelors"].shape[0]
    percentage_bachelors = round((total_bachelors / total_rows) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    total_adv_ed = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])].shape[0]
    total_adv_ed_m50k = df[(df["education"].isin(["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")].shape[0]

    # What percentage of people without advanced education make more than 50K?
    total_low_ed = df[~(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))].shape[0]
    total_low_ed_m50k = df[~(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))& (df["salary"] == ">50K")].shape[0]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(total_adv_ed_m50k / total_adv_ed * 100, 1)
    lower_education = round(total_low_ed_m50k / total_low_ed * 100, 1)

    # percentage with salary >50K
    higher_education_rich = round(total_adv_ed_m50k / total_adv_ed * 100, 1) ########
    lower_education_rich = round(total_low_ed_m50k / total_low_ed * 100, 1) #######

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_less_min = df[(df["hours-per-week"] == df["hours-per-week"].min())].shape[0]
    total_less_min_rich = df[(df["hours-per-week"] == df["hours-per-week"].min()) & (df["salary"] == ">50K")].shape[0]

    num_min_workers = df[(df["hours-per-week"] == df["hours-per-week"].min())].shape[0]

    rich_percentage = round(total_less_min_rich / total_less_min * 100, 1)  #######

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (( df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts() ) * 100 ).idxmax()
    highest_earning_country_percentage = (( df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts() ) * 100 ).max().round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

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
