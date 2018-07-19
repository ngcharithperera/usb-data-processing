class DataRecord(object):
    observation_id = ""
    sensor_id = ""
    platform_id = ""
    ObservableProperty = ""
    timestamp = ""

    building_floor = ""

    results_numeric_value = ""
    results_unit = "" 
    results_data_type = ""

    def __init__(self, 
                 observation_id, 
                 sensor_id, 
                 platform_id,
                 ObservableProperty,
                 timestamp,
                 building_floor,
                 results_numeric_value,
                 results_unit,
                 results_data_type):
        self.observation_id = observation_id
        self.sensor_id = sensor_id
        self.platform_id = platform_id
        self.ObservableProperty = ObservableProperty
        self.timestamp = timestamp
        self.building_floor = building_floor
        self.results_numeric_value = results_numeric_value
        self.results_unit = results_unit
        self.results_data_type = results_data_type



