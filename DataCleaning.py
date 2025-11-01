import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt


path = "./Datasets/Raw/"

# DataLoading
Appointments = pd.read_csv(path + "appointments.csv")
Patients = pd.read_csv(path + "patients.csv")
Slots = pd.read_csv(path + "slots.csv")
# print(f"the appointments.csv feature are {Appointments.columns}")
# print(Patients.columns)
# print(Slots.columns)


"""
# handing the appointment.csv

"""
Appointments_dup = Appointments
Patients_dup = Patients
Slots_dup = Slots

# print(Appointments_dup.columns)
# print(f" the total rows are: {Appointments_dup.shape[0]}")
# print("\n")


def Find_NaN(DataFrame, name="DataFrame"):

    total_rows = DataFrame.shape[0]
    na_sum = DataFrame.isna().sum()
    na_percentage = ((na_sum / total_rows) * 100).round(2)

    stats = {
        "total_rows": total_rows,
        "na_counts": na_sum,
        "na_percentage": na_percentage,
    }

    print(f" the total rows of {name} are: {total_rows}")
    print("\n")
    print(
        f"the overview of NaN value:\n {pd.DataFrame({'total NaN values': na_sum,'the percentage of NaN %':na_percentage})}"
    )
    print("==============================")
    # 缺失值条形图
    msno.bar(DataFrame)
    plt.show()

    return stats


Find_NaN(Appointments_dup, name="Appointments_dup")
Find_NaN(Patients_dup, name="Patients_dup")
Find_NaN(Slots_dup, name="Slot_dup")
