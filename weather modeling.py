def temperature_modeling(a, b, c, time):
    temperature = a * time**2 + b * time + c
    return temperature
a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10
print("Step 1: Hard-coded Variables for Weather Modeling")
time_hardcoded = 5  
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
print("\n")
a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))
time_keyboard = float(input("Enter time in hours: "))
print("Step 2: Keyboard Input for Weather Modeling")
print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
print("\n")
with open('weather_coefficients.txt', 'r') as file:
    lines = file.readlines()
    a_file, b_file, c_file, time_file = map(float, lines[0].split())
print("Step 3: Read from a File for Weather Modeling")
print("Temperature for file input coefficients at time", time_file, "hours:", temperature_modeling(a_file, b_file, c_file, time_file))
print("\n")
print("Step 4: Single Set of Input for Weather Modeling")
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
print("\n")
with open('multiple_weather_coefficients.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        a_multi, b_multi, c_multi, time_multi = map(float, line.split())
        print("Temperature for multiple set coefficients at time", time_multi, "hours:", temperature_modeling(a_multi, b_multi, c_multi, time_multi))
print("\n")
