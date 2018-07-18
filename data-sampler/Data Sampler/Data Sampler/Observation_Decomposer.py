observation_id = ""
sensor_id = ""
platform_id = ""
ObservableProperty = ""
timestamp = ""

results_numeric_value = ""
results_unit = ""
results_data_type = ""

def Decompose(parsed_json):
    results_numeric_value = results_numeric_value_extractor(parsed_json)
    results_unit = results_unit_extractor(parsed_json)
    ObservableProperty = ObservableProperty_extractor(parsed_json)
    timestamp = timestamp_extractor(parsed_json)
    results_data_type = results_data_type_extractor(parsed_json)
    print(parsed_json)



# results_numeric_value
def results_numeric_value_extractor(parsed_json):
    results_numeric_value = parsed_json["data"]["timeseries"]["value"]["data"]
    #print(results_numeric_value)
    return results_numeric_value

#results_unit
def results_unit_extractor(parsed_json):
    results_unit = parsed_json["data"]["timeseries"]["unit"]
    #print(results_unit)
    return results_unit

#ObservableProperty
def ObservableProperty_extractor(parsed_json):
    ObservableProperty = parsed_json["data"]["feed"]["metric"]
    #print(results_numeric_value)
    return ObservableProperty

#timestamp
def timestamp_extractor(parsed_json):
    timestamp = parsed_json["data"]["timeseries"]["value"]["time"]
    #print(timestamp)
    return timestamp

#results_data_type
def results_data_type_extractor(parsed_json):
    results_data_type = parsed_json["data"]["timeseries"]["value"]["type"]
    #print(results_data_type)
    if results_data_type == "Real":
        results_data_type = "Double"
    return results_data_type