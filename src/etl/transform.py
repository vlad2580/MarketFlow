import pandas as pd

def remove_duplicates(data):
    """
    Removes duplicates from DataFrame.

    Arguments:
    - data (DataFrame): original data.

    Returns:
    - DataFrame: data without duplicates.
    """
    initial_length = len(data)
    data_without_duplicates = data.drop_duplicates()
    final_length = len(data_without_duplicates)
    
    print(f"Delited {initial_length - final_length} duplicates.")
    
    return data_without_duplicates

def group_by_product_and_sum(data):
    return data.groupby('Product line')['Total'].sum().reset_index()




    
if __name__ == "__main__":
    from extract import extract_data

    filepath = "data/raw/supermarket_sales - Sheet1.csv"
    raw_data = extract_data(filepath)

    if raw_data is not None:
        raw_data['Date'] = pd.to_datetime(raw_data['Date'])
        filtered_data = raw_data[(raw_data['Date'] >= '2019-01-09') & (raw_data['Date'] <= '2019-11-30') & (raw_data['Rating'] > 7.5)]
        transformed_data = remove_duplicates(filtered_data)
        result = group_by_product_and_sum(transformed_data)
        print(result)
    else:
        print("Ошибка извлечения данных. Невозможно продолжить трансформацию.")

