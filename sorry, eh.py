import JSON_data
import data_analytics
import compiler

link1 = "C:/Users/ukapo/Desktop/QHACKS/testData.json"
link2 = "C:/Users/ukapo/Desktop/QHACKS/dataAnalytics.json"

data_An = JSON_data.data_import(link2)
data_test = JSON_data.data_import(link1)

#Get the following data from webpage
#cat, sub_cat, name, reason = get_web.get_data()
cat = "professional"
sub_cat = "boss"
name = "Mr. T"
reason = "not showing up to the meeting"
#get it

tupleA = data_analytics.recommending_engine(cat, sub_cat)

first1 = tupleA[0][0] #line one
second1 = tupleA[1][0]
third1 = tupleA[2][0]

first2 = tupleA[0][1] #line two
second2 = tupleA[1][1]
third2 = tupleA[2][1]

firstPer = tupleA[0][2] * 100 #percentage probability
secondPer = tupleA[1][2] * 100
thirdPer = tupleA[2][2] * 100

best_apology = compiler.create_apology(cat, sub_cat, first1, first2, name, reason)
second_best_apology = compiler.create_apology(cat, sub_cat, second1, second2, name, reason)
third_best_apology = compiler.create_apology(cat, sub_cat, third1, third2, name, reason)

print(best_apology)
print("\nThis worked", firstPer * 100, "% of the time.")
print()
print(second_best_apology)
print("\nThis worked", secondPer * 100, "% of the time.")
print()
print(third_best_apology)
print("\nThis worked", thirdPer * 100, "% of the time.")

