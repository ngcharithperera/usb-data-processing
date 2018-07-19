import json
import Observation_Decomposer

allowed_floor_number = ['6']

def floor_filter(parsed_json):
    #print(parsed_json)
    if parsed_json["signal"] == 2:   
        try:
            floor_number = parsed_json["data"]["entity"]["meta"]["buildingFloor"]
            if floor_number in allowed_floor_number:
                Observation_Decomposer.Decompose(parsed_json)
                print(floor_number)
                with open('data.json', 'a') as outfile:
                    json.dump(parsed_json, outfile)
        except Exception as e:  
            print(e)
            pass
            #print("No Floor")

        
            