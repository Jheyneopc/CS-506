#Find unique values in a dictionary*
def unique_dict_values(data):
    unique = set()
    for item in data:
        for value in item.values():
            unique.add(value)
    print("Unique Values:", unique)

sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
               {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_dict_values(sample_data)

