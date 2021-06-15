N = int(input())
medicineDict = {}
for _ in range(N):
    effect, medicine = map(int, input().split())
    medicineDict[effect] = medicine
R = int(input())
for _ in range(R):
    symptoms = list(map(int, input().split()))
    symptomToMedicine = []
    for i in range(symptoms[0]):
        if medicineDict.get(symptoms[i+1]) == None:
            symptomToMedicine = ["YOU DIED"]
            break
        symptomToMedicine.append(medicineDict[symptoms[i+1]])
    print(*symptomToMedicine)