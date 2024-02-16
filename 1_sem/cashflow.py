import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse


def cashflow_analysis(month, year):
    if int(month) < 1 or int(month) > 12:
        raise ValueError('month number must be between 01 and 12')

    if int(year) > 2024:
        raise ValueError("year number can't be greater than current")

    outcome_data = pd.read_excel(f"D:/User/Downloads/Telegram Desktop/infa_sem1_{month}_{year}.xlsx")

    outcome_data["День"] = [int(x.split()[0]) for x in outcome_data["Дата"]]

    fig, ax = plt.subplots(constrained_layout=True)

    sns.barplot(
        data=outcome_data,
        y="Категория",
        x="Сумма",
        orient="h",
        estimator="sum",
        errorbar=None,
        ax=ax
    )
    plt.title(label=f'Расходы за {month}.{year}')
    plt.savefig('cashflow.png')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='processing month and year')
    parser.add_argument('month', type=str, help='month in format "mm"')
    parser.add_argument('year', type=str, help='year in format "yyyy"')
    args = parser.parse_args()

    cashflow_analysis(args.month, args.year)
