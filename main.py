from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    # Ejecuta el análisis y muestra resultados (si print_data=True en la función)
    results = calculate_demographic_data(print_data=True)

    # Muestra llaves principales para inspección rápida
    print("\nClaves retornadas:", list(results.keys()))
