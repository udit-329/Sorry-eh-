import JSON_data

link = "C:\\Users\\patri\\OneDrive\\Desktop\\flask\\dataAnalytics.json"
data = JSON_data.data_import(link)

def add_data(cat, sub_cat, ss, se, work_or_not):

    var_count = "count" + str(ss) + str(se)
    data[cat][sub_cat][var_count] += 1

    if (work_or_not):
        var_data = "ss" + str(ss) + "_se" + str(se)
        data[cat][sub_cat][var_data] += 1

    JSON_data.data_export(link, data)

def recommending_engine(cat, sub_cat):#return first, second, third

    f1 = data[cat][sub_cat]["ss1_se1"] / data[cat][sub_cat]["count11"]
    f2 = data[cat][sub_cat]["ss1_se2"] / data[cat][sub_cat]["count12"]
    f3 = data[cat][sub_cat]["ss2_se1"] / data[cat][sub_cat]["count21"]
    f4 = data[cat][sub_cat]["ss2_se2"] / data[cat][sub_cat]["count22"]

    t1 = f1
    t2 = f2
    t3 = f3
    t4 = f4

    a = [t1,t2,t3,t4]

    a.sort()

    if(f1 == a[3]):
        first = (1, 1, f1)
    elif(f2 == a[3]):
        first = (1, 2, f2)
    elif(f3 == a[3]):
        first = (2, 1, f3)
    elif(f4 == a[3]):
        first = (2, 2, f4)

    if(f1 == a[2]):
        second = (1, 1, f1)
    elif(f2 == a[2]):
        second = (1, 2, f2)
    elif(f3 == a[2]):
        second = (2, 1, f3)
    elif(f4 == a[2]):
        second = (2, 2, f4)

    if(f1 == a[1]):
        third = (1, 1, f1)
    elif(f2 == a[1]):
        third = (1, 2, f2)
    elif(f3 == a[1]):
        third = (2, 1, f3)
    elif(f4 == a[1]):
        third = (2, 2, f4)

    return (first, second, third)




