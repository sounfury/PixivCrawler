# -Time :2023/2/14 13:41
# -*- codeing =utf-8 -*-
import search
import painter
import rank
if __name__=='__main__':
    a=input("请选择1.搜索tag   2.搜索画师     3.排行榜")
    if int(a)==1:
        search.search__()
    elif int(a)==2:
        painter.painter__()
    elif int(a) == 3:
        rank.rank__()





