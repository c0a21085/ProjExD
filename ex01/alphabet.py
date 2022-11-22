import random
import datetime
word_count = 10
word_loss = 3
max_count = 0

def words():
    word_list = []
    word_num = random.sample(list(range(65, 91)), word_count)
    print("対象文字：")
    for num in word_num:
        word_list.append(chr(num))
        print(chr(num), end = " ")
    #print(word_list)
    print("")
    return word_list

def words_loss(word_list):
    ans_words = []
    print("表示文字：")
    for i in range(word_loss):
        ans_words += word_list.pop(random.randint(0, len(word_list)-1))
    for word in word_list:
        print(word, end = " ")
    print("")
    random.shuffle(ans_words)
    return ans_words

def word_quiz(ans_words):
    global max_count
    st = datetime.datetime.now()
    ans_numloss = int(input("欠損文字はいくつあるでしょうか？："))
    if ans_numloss == len(ans_words):
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください。")
        word_count = len(ans_words)
        for i in range(word_count):
            ans = str.upper(input(f"{i+1}つ目の文字を大文字または小文字で入力してください："))
            if ans in ans_words:
                max_count += 1
                ans_words.remove(ans)
            else:
                print("不正解です、またチャレンジしてください")
                break
            if len(ans_words) == 0:
                print("正解です！！！")
    else:
        print("不正解です、またチャレンジしてください。")
    ed = datetime.datetime.now()
    print(f"所要時間：{(ed-st).seconds}")

if __name__ == "__main__":
    word_quiz(words_loss(words()))