import pandas as pd

def calculate_demographic_data(print_data: bool = True):
    """
    Analiza el dataset (adult.data.csv) y devuelve un diccionario con:
      - race_count (Series)
      - average_age_men (float, 1 decimal)
      - percentage_bachelors (float, 1 decimal)
      - higher_education_rich (float, 1 decimal)
      - lower_education_rich (float, 1 decimal)
      - min_work_hours (int)
      - rich_percentage (float, 1 decimal)
      - highest_earning_country (str)
      - highest_earning_country_percentage (float, 1 decimal)
      - top_IN_occupation (str)
    """
    # Cargar datos (nombre estándar del starter FCC)
    df = pd.read_csv("adult.data.csv")

    # 1) Conteo por raza
    race_count = df["race"].value_counts()

    # 2) Promedio de edad de los hombres
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # 3) Porcentaje de personas con Bachelors
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4) Porcentaje >50K con educación avanzada (Bachelors, Masters, Doctorate)
    higher_ed = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round((df.loc[higher_ed, "salary"] == ">50K").mean() * 100, 1)

    # 5) Porcentaje >50K sin educación avanzada
    lower_education_rich = round((df.loc[~higher_ed, "salary"] == ">50K").mean() * 100, 1)

    # 6) Mínimo de horas trabajadas por semana
    min_work_hours = int(df["hours-per-week"].min())

    # 7) Porcentaje de personas que trabajan min horas y ganan >50K
    min_workers = df["hours-per-week"] == min_work_hours
    rich_percentage = round((df.loc[min_workers, "salary"] == ">50K").mean() * 100, 1)

    # 8) País con mayor % de >50K y ese porcentaje
    #    Para cada país: (# >50K) / (total país)
    country_counts = df["native-country"].value_counts()
    country_rich_counts = df.loc[df["salary"] == ">50K", "native-country"].value_counts()
    pct_by_country = (country_rich_counts / country_counts * 100).dropna()
    highest_earning_country = pct_by_country.idxmax()
    highest_earning_country_percentage = round(pct_by_country.max(), 1)

    # 9) Ocupación más común para >50K en India
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print("Min work time:", min_work_hours, "hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }

# Self-test opcional al ejecutar directamente
if __name__ == "__main__":
    try:
        calculate_demographic_data(print_data=True)
        print("\nSelf-test OK.")
    except FileNotFoundError:
        print("No se encontró 'adult.data.csv'. Asegúrate de que el dataset está en la raíz.")
