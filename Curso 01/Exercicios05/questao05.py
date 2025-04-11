def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solicitar a temperatura em Celsius ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converter para Fahrenheit
fahrenheit = celsius_para_fahrenheit(celsius)

print(f"A temperatura de {celsius}°C é igual a {fahrenheit}°F.")
