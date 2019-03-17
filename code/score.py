def initial_std():
    return{
            "554145301":{
                "name": "นางสาว จริยา อินทร์ดา", 
                "score": 25
                },
            "554145302":{
                "name": "นาย จักรกิช แก้วเฌร",
                "score": 15
                },
            "554145303": {
                "name": "นาย จักรี เหมณี",
                "score": 22
                }
        }
def add_std(std_list):
    std_id = input("ID: ")
    name = input("Name: ")
    score = int(input("Score: "))
    std_list[std_id] = {"name": name, "score": score}
    return std_list

def remove_std(std_list):
    std_id = input("ID: ")
    if std_id in std_list:
        del std_list[std_id] 
    return std_list

def mean_score(std_list):
    tmp = [std_list[i]["score"] for i in std_list.keys()]
    return sum(tmp)/len(tmp)

#Main()
list_of_student = initial_std()

