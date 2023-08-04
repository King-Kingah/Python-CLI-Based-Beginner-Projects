# Simple Python application to calculate body-mass-index(BMI)

weight = float(input(f"Enter your weight in kilos: "))
height = float(input(f"Enter your height in meters: "))

def getBMI(weight, height):
    BMI = weight / (pow(height, 2)) # calculate BMI
    classification = ["Under Weight", "Normal", "Over Weight", "Obesity - Class I", "Obesity - Class II", "Extreme Obesity"]

    if (BMI < 18.5):
        print(f"Your BMI is {round(BMI, 2)}\nClassification: {classification[0]}")
    elif (18.5 < BMI < 24.9):
        print(f"Your BMI is {round(BMI, 2)}\nClassification: {classification[1]}")
    elif (25 < BMI < 29.9):
        print(f"Your BMI is {round(BMI, 2)}\nClassification: {classification[2]}")
    elif (30 < BMI < 34.9):
        print(f"Your BMI is {round(BMI, 2)}\nClassification: {classification[3]}")
    elif (35 < BMI < 39.9):
        print(f"Your BMI is {round(BMI, 2)}\nClassification: {classification[4]}")
    else:
        print(f"Your BMI is {round(BMI, 2)}\nClassification: {classification[5]}")

    return BMI;

getBMI(weight, height)
# print(type(weight))
# print(type(height))

# TO DO: