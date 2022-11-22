import random
import datetime
#quiz_num = 0

def shutudai(quiz_list):
    #global quiz_num
    #print("問題：")
    #quiz_num = random.randint(-1, 2)
    #print(quiz_list[quiz_num]) 
    qa = random.choice(quiz_list)
    print("問題：" + qa["q"])
    return qa["a"]

def kaitou(ans_list):
    st = datetime.datetime.now()
    #print(st)
    ans = input("答えるんだ：")
    #if ans in ans_list[quiz_num]:
    if ans in ans_list:
       print("正解！！！")
    else:
        print("出直してこい")
    ed = datetime.datetime.now()
    #print(ed)
    print(f"時間:{(ed-st).seconds}")

if __name__ == "__main__":
    #quiz_list = ["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"]
    #ans_list = [["マスオ", "ますお"],["ワカメ", "わかめ"],["甥", "おい", "甥っ子", "おいっこ"]]
    quiz_list = [{"q":"サザエさんの旦那の名前は？","a":["マスオ", "ますお"]},
                 {"q":"カツオの妹の名前は？", "a": ["ワカメ", "わかめ"]},
                 {"q":"タラオはカツオから見てどんな関係？", "a":["甥", "おい", "甥っ子", "おいっこ"]}]
    #shutudai(quiz_list)
    kaitou(shutudai(quiz_list))