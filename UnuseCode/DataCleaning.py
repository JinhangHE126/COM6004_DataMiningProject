import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt


path = "./Datasets/Raw/"

# DataLoading
survey = pd.read_csv(path + "survey.csv")
# print(f"the appointments.csv feature are {Appointments.columns}")
# print(Patients.columns)
# print(Slots.columns)


"""
# handing the raw datasets

"""
survey_dup = survey

# print(Appointments_dup.columns)
# print(f" the total rows are: {Appointments_dup.shape[0]}")
# print("\n")


def Find_NaN(DataFrame, name="DataFrame"):
    """Find the NaN value in individual file

    Args:
        DataFrame (DataFrame): _description_
        name (str, optional): _description_. Defaults to "DataFrame".

    Returns:
        _type_: _description_
    """

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
    print("===============================================")
    # 缺失值条形图
    msno.bar(DataFrame)
    plt.show()

    return stats
