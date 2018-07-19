import re

observation_id = ""
sensor_id = ""
platform_id = ""
ObservableProperty = ""
timestamp = ""

building_floor = ""

results_numeric_value = ""
results_unit = ""
results_data_type = ""

def Decompose(parsed_json):
    results_numeric_value = results_numeric_value_extractor(parsed_json)
    results_unit = results_unit_extractor(parsed_json)
    ObservableProperty = ObservableProperty_extractor(parsed_json)
    timestamp = timestamp_extractor(parsed_json)
    results_data_type = results_data_type_extractor(parsed_json)
    building_floor = building_floor_extractor(parsed_json)


    sensor_id = sensor_id_extractor(parsed_json)
    platform_id = platform_id_creator(parsed_json)
    observation_id = observation_id_creator(parsed_json)
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

#building_floor
def building_floor_extractor(parsed_json):
    try:
        building_floor = parsed_json["data"]["entity"]["meta"]["buildingFloor"]
        #print(building_floor)
    except: 
        building_floor = "NA"
        pass
        #print("No Floor")
    return building_floor


#sensor_id
def sensor_id_extractor(parsed_json):
    sensor_id = parsed_json["data"]["brokerage"]["id"].replace("\'", "")
    #print(sensor_id)
    return sensor_id


#platform_id
def platform_id_creator(parsed_json):
    platform_id = parsed_json["data"]["brokerage"]["broker"]["id"].replace("-", "") + parsed_json["data"]["brokerage"]["id"].replace("\'", "")
    #print(platform_id)
    return platform_id


#observation_id
def observation_id_creator(parsed_json):
    observation_id = parsed_json["data"]["timeseries"]["value"]["time"].replace("-", "").replace(":", "").replace(".", "").replace(" ", "") + parsed_json["data"]["feed"]["metric"]
    #print(observation_id)
    return observation_id