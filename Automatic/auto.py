import datetime

# 获取时间
curr_time = datetime.datetime.now()
new_time = curr_time.strftime("%Y年%m月%d日")
day = int(curr_time.strftime("%d")) - 1
muth = curr_time.strftime("%m")
print(new_time)
print(day)
new_str = f'2021年1月12日  --  {muth}月{day}日 目标   完成  \n{new_time}目标 \n1，早7点5分起床\n2，python学习两个章节 \n3，模拟选择题基础部分做一遍 \n4，在家运动30分钟'
print(new_str)
# 打开文件
fo = open("xinxin.txt", "w+" ,encoding='utf-8')
# 读取文件所有内容
fo.write(new_str)
# 关闭文件
fo.close()