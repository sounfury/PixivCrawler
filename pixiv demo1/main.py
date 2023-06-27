# -Time :2023/2/14 13:41
# -*- codeing =utf-8 -*-
import search
import painter
import rank
def main():
    while True:
        print("请选择：")
        print("1.搜索tag")
        print("2.搜索画师")
        print("3.排行榜")
        a = input("请输入你的选择（数字1-3）：")
        if a == "1":
            search.search__()
            break
        elif a == "2":
            painter.painter__()
            break
        elif a == "3":
            rank.rank__()
            break
        else:
            print("无效的输入，请输入1，2或3")

if __name__=='__main__':
    main()





