def group_values_by_key(data_list):
    """
    Groups values by their keys from a list of dictionaries.
    
    Args:
    - data_list (list of dict): A list of dictionaries with potentially overlapping keys.

    Returns:
    - dict: A dictionary where each key is unique across all input dictionaries, and the value is a list of values
            from all dictionaries that contain that key.
    """
    grouped_data = {}
    for item in data_list:
        for key, value in item.items():
            if key not in grouped_data:
                grouped_data[key] = [value]
            else:
                grouped_data[key].append(value)
    return grouped_data
