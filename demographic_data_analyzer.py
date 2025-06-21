import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education (Bachelors, Masters, Doctorate)
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    # 5. % >50K with advanced education
    higher_edu_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1)

    # 6. % >50K without advanced education
    lower_edu_rich = round(
        (df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    # 7. Min hours per week
    min_hours = df['hours-per-week'].min()

    # 8. % working min hours with >50K
    min_hour_workers = df[df['hours-per-week'] == min_hours]
    rich_min_hour = round(
        (min_hour_workers['salary'] == '>50K').mean() * 100, 1)

    # 9. Country with highest % of >50K
    rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    country_percent = (rich_country / total_country * 100).dropna()
    highest_country = country_percent.idxmax()
    highest_percent = round(country_percent.max(), 1)

    # 10. Most popular >50K occupation in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_india_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_edu_rich}%")
        print("Min work hours per week:", min_hours)
        print(f"Rich among those who work fewest hours: {rich_min_hour}%")
        print("Country with highest % rich:", highest_country, f"({highest_percent}%)")
        print("Top occupation in India for >50K earners:", top_india_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage_min_hours': rich_min_hour,
        'highest_earning_country': highest_country,
        'highest_earning_country_percentage': highest_percent,
        'top_IN_occupation': top_india_occupation
    }
