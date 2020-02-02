"""
Auth: Patrick Jung
Date: February 2, 2020
Desc: Python script that implements functions to a project using Firebase
"""

from firebase import firebase

class FirebaseApp:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication("https://apologycombtndb.firebaseio.com/", None)

    def __sanitize(self, string):
        return string.strip().lower()

    def insert(self, section, subsection, str_list):
        """
        insert(section : str, subsection : str, str_list : List[str])

        Inserts strings from a list into a Firebase directory defined as "/<section>/<subsection>"
        """
        section = self.__sanitize(section)
        subsection = self.__sanitize(subsection)

        str_dict = {}
        for index, str_new in enumerate(str_list):
            str_dict['string_' + str(index)] = str_new
        try:
            res = self.firebase.post('/%s/%s' % (section, subsection), str_dict)
            print(res)
        except Exception:
            print("Unauthorized Insertion: " + section + ", " + subsection + ", " + str(str_list))

    def retrieve(self, section, subsection = ""):
        """
        retrieve(section : str, subsection : str) : List[Tuple[str]]

        Gets all string combinations from the lowest levels of a Firebase directory
        defined as "/<section>/<subsection>", returning them as string tuples in a list
        """
        def dfs_append(x, str_res = [], depth = 0):
            for value in x.values():
                if type(value) != str:
                    dfs_append(value, str_res, depth + 1)
                    continue
                str_res.append(tuple(x.values()))
                break
            if not depth:
                return str_res
            #if type(x) == str:
                #str_res.append(x)
                #return
            #for value in x.values():
                #dfs_append(value, str_res, depth + 1)
            #if not depth:
                #return str_res

        section = self.__sanitize(section)
        subsection = self.__sanitize(subsection)

        try:
            res = self.firebase.get('/%s/%s' % (section, subsection), '')
            return dfs_append(res)
        except Exception:
            print("Unauthorized Retrieval: " + section + ", " + subsection)

    def delete(self, section, subsection = ""):
        """
        delete(section : str, subsection : str)

        Deletes everything from a Firebase directory defined as "/<section>/<subsection>"
        """
        section = self.__sanitize(section)
        subsection = self.__sanitize(subsection)

        res = self.firebase.get('/%s/%s' % (section, subsection), '')
        try:
            for key in res.keys():
                self.firebase.delete('/%s/%s' % (section, subsection), key)
        except Exception:
            print("Unauthorized Deletion: " + section + ", " + subsection)

    def count_combtns(self, combtn_list):
        """
        count_combtns(combtn_list : List[x]) : List[Tuple[str]]

        Counts the number of elements for every unique element in the combination list,
        returning these element counts as a list of 2-length tuples
        """
        if combtn_list:
            combtn_dict = {}
            for combtn in combtn_list:
                if (combtn in combtn_dict):
                    combtn_dict[combtn] += 1
                else:
                    combtn_dict[combtn] = 1
            return list(combtn_dict.items())
        return []

def test_open_link(self, link):
    """
    test_open_link(link : str)

    Tests by opening up a link to a link.
    """
    import os
    os.system("start \"\" " + link)

if __name__ == "__main__":
    """
    This header content represents CombtnDB's main-line logic
    """
    firebase_app = FirebaseApp()
    #firebase_app.insert("work", "friend", ["i'm sorry", "i apologize", "i messed up"])
    #firebase_app.insert("work", "friend", ["i was stupid"])

    #firebase_app.insert("work", "worker", ["i'm so sorry!!!!"])
    #firebase_app.insert("work", "worker", ["can i have your number"])

    #firebase_app.insert("relationships", "relationship", ["oh noes"])
    #firebase_app.insert("relationships", "", ["oh yes"])

    #print(firebase_app.count_combtns(firebase_app.retrieve("work", "friend")))

    #firebase_app.delete("")
    pass