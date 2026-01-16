import pandas as pd


def process_csv_in_chunks(file_path, column, treshold, chunksize=1000):
    total_count = 0
    sum_values = 0

    for chunk in pd.read_csv(file_path, chunksize=chunksize, usecols=[column]):
        chunk[column] = pd.to_numeric(chunk[column], errors="coerce")
        filtered = chunk[(chunk[column] > treshold) & (~chunk[column].isna())]
        total_count = len(filtered)
        sum_values = filtered[column].sum()

    # return a tuple
    return total_count, sum_values


if __name__ == "__main__":
    file_path = "./files/survey_results_public.csv"
    column = "YearsCode"
    treshold = 10

    total_counts, sum_values = process_csv_in_chunks(file_path, column, treshold)
    average = sum_values / total_counts if total_counts > 0 else 0

    print(f"Total counts {total_counts}")
    print(f"Sum values {sum_values}")
    print(f"Avg {average}")
