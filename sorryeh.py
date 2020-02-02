def test_open_link(link):
    """
    test_open_link(link : str)

    Tests by opening up a link to a link.
    """
    import os
    os.system("start \"\" " + link)

def analyze(cat, sub_cat, name, reason):
    #test_open_link("cat=" + cat + ";sub_cat=" + sub_cat + ";name=" + name + ";reason=" + reason)
    #return ("best_out", "second_out", "third_out", 91, 77, 53)

    import JSON_data
    import data_analytics
    import compiler

    link1 = "C:\\Users\\patri\\OneDrive\\Desktop\\flask\\testData.json"
    link2 = "C:\\Users\\patri\\OneDrive\\Desktop\\flask\\dataAnalytics.json"

    data_An = JSON_data.data_import(link2)
    data_test = JSON_data.data_import(link1)

    #Get the following data from webpage
    #get it

    tupleA = data_analytics.recommending_engine(cat, sub_cat)

    first1 = tupleA[0][0] #line one
    second1 = tupleA[1][0]
    third1 = tupleA[2][0]

    first2 = tupleA[0][1] #line two
    second2 = tupleA[1][1]
    third2 = tupleA[2][1]

    firstPer = tupleA[0][2] #percentage probability
    secondPer = tupleA[1][2]
    thirdPer = tupleA[2][2]

    best_apology = compiler.create_apology(cat, sub_cat, first1, first2, name, reason)
    second_best_apology = compiler.create_apology(cat, sub_cat, second1, second2, name, reason)
    third_best_apology = compiler.create_apology(cat, sub_cat, third1, third2, name, reason)
    #test_open_link(best_apology + " " + second_best_apology + " " + third_best_apology)

    return (best_apology, second_best_apology, third_best_apology, firstPer, secondPer, thirdPer)