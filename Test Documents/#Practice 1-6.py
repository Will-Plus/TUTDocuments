#Practice 1-6 编写程序，输入10个学生的成绩，按三档进行统计，80~100--A 60~79--B 60以下为C，再将各档等级为键，对应人数为值，将这些数据保存到一个字典中
def classify_grades(grades):
    # 初始化结果字典
    grade_distribution = {"A": 0, "B": 0, "C": 0}
    
    # 分类成绩
    for grade in grades:
        if 80<=grade<=100:
            grade_distribution["A"]+=1
        elif 60<=grade<=79:
            grade_distribution["B"]+=1
        elif grade<60:
            grade_distribution["C"]+=1
    return grade_distribution
# 输入 10 个学生的成绩
grades = []
print("请输入10个学生的成绩（0-100）：")
for i in range(10):
    while True:
        try:
            grade=int(input(f"第 {i+1} 个学生的成绩: "))
            if 0<=grade<=100:
                grades.append(grade)
                break
            else:
                print("成绩必须在0到100之间，请重新输入。")
        except ValueError:
            print("请输入有效的数字。")
# 统计成绩等级分布
result = classify_grades(grades)
# 输出结果
print("成绩等级分布统计如下：")
print(result)