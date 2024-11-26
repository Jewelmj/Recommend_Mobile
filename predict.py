import numpy
import pandas as pd
from search import filter_1
def predict_1(input_from_user):
    user_mobile_sp = {"Total_storage":input_from_user["Total_storage"],
                "Back_Mpx":input_from_user["Back_Mpx"],
                "Ram":input_from_user["Ram"],
            }
    result_sep = {"Total_storage":user_mobile_sp["Total_storage"],
                "Back_Mpx":user_mobile_sp["Back_Mpx"],
                "Ram":user_mobile_sp["Ram"],
                }

    age_sep = {"Total_storage":50,
    "image_storage(Taken from camera)":3,
    "Application_storage":20,
    }
            
    user_inputs = {"Total_storage":input_from_user["Total_storage_used"],
                "image_storage(Taken from camera)":input_from_user["image_storage_used"],
                "Application_storage":input_from_user["Application_storage_used"],
            }

    range_limts = {"Total_storage":[10,15,20,25,30],
                    "image_storage(Taken from camera)":[0.4,0.8,1.1,1.5,2],
                    "Application_storage":[15,20,25,30,35]}
    extra = [0,0,0]
    points = {"Total_storage":0,
            "image_storage(Taken from camera)":0,
            "Application_storage":0,
            }
    ratei =0
    # variables for loops
    i=0
    #for the storage
    # def making_dic():
    def Algo():
        def increase_pix():
            back_list_of_types = [12,32,48,64,108]
            if not back_list_of_types[4] <= user_mobile_sp["Back_Mpx"]:
                for b_i in back_list_of_types:
                    indexs = back_list_of_types.index(b_i)
                    if b_i == user_mobile_sp["Back_Mpx"] and indexs <4:
                        result_sep["Back_Mpx"] = back_list_of_types[indexs+1]
                        break
            else:
                result_sep["Back_Mpx"] = back_list_of_types[4]
                
        def increase_storage():
            list_range_storage = [32,64,128,256,512]
            if not list_range_storage[4] <= user_mobile_sp["Total_storage"]:
                for s_i in list_range_storage:
                    indexs = list_range_storage.index(s_i)
                    if s_i == user_mobile_sp["Total_storage"]:
                        result_sep["Total_storage"] = list_range_storage[indexs+1]
                        break
            else:
                result_sep["Total_storage"] = list_range_storage[4]
        def increase_Ram():
            list_range_Ram = [4,6,8,12]
            if not list_range_Ram[3] <= user_mobile_sp["Ram"]:
                for R_i in list_range_Ram:
                    indexs = list_range_Ram.index(R_i)
                    if R_i == user_mobile_sp["Ram"] and indexs < 3:
                        result_sep["Ram"] = list_range_Ram[indexs+1]
                        break
            else:
                result_sep["Ram"] = list_range_Ram[3]
            result_sep["Ram"] = result_sep["Ram"]*1000

        # def def_points(values = {}):
        def points_dic():
            for xx in user_inputs:
                if user_inputs[xx] > age_sep[xx]:
                    indexs = list(user_inputs.keys()).index(xx)
                    extra[indexs] = user_inputs[xx] - age_sep[xx]
                    
            for loo in range_limts:
                indexs = list(range_limts.keys()).index(loo)
                for loo2 in range_limts[loo]:
                    indexs2 = list(range_limts[loo]).index(loo2)
                    if loo2 < extra[indexs]:
                        points[loo] += 1 
        points_dic()           
        for value in points:
            if points[value] != 0:
                if value == "Total_storage":
                    increase_storage()
                if value == "image_storage(Taken from camera)":
                    increase_pix()
                if value == "Application_storage":
                    increase_Ram()
        print(points)
        print(result_sep)
        if result_sep["Ram"] <4000:
            result_sep["Ram"] = result_sep["Ram"]*1000
        filter_1(result_sep)
    Algo()  