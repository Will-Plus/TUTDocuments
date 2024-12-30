#Practice 1-2 判断今天是今年的第几天
from datetime import datetime
def day_of_year():
    # 获取今天的日期
    today = datetime.today()
    # 计算今天是今年的第几天
    day_of_year = today.timetuple().tm_yday
    return today, day_of_year
# 调用函数
today, day_number = day_of_year()
# 输出结果
print(f"今天是 {today.strftime('%Y-%m-%d')}，是今年的第 {day_number} 天。")