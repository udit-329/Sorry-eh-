import JSON_data

link1 = "C:/Users/ukapo/Desktop/QHACKS/testData.json"
link2 = "C:/Users/ukapo/Desktop/QHACKS/generic_part.json"
data = JSON_data.data_import(link1)
generic = JSON_data.data_import(link2)

def get_sentences(cat, sub_cat, ss, se):
    sen1 = data[cat][sub_cat][ss - 1]
    sen2 = data[cat][sub_cat][se + 1]

    return sen1, sen2

def create_apology(cat, sub_cat, ss, se, name, reason):
    
    sen1, sen2 = get_sentences(cat, sub_cat, ss, se)
    gen_part = generic[cat]
    if(cat == "SO"):
        apology = name + ", " + sen1 + gen_part + reason + ". " + sen2
    else:
        apology = name + ", " + sen1 + reason + ". " + gen_part + sen2
        
    return apology
