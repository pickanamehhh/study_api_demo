# 正则 python中的正则操作  从一个大文本中匹配需要的信息
# 两个知识点支撑
# 第一个：正则表达式中元字符的理解
# 第二个：
import re

str1 = '1234abcd5678'

# 先创建pattern对象
pattern = re.compile('12\d4')  # \d 0--9

result = re.match(pattern, str1)  # match()匹配以指定的模块开头的字符串
print(result.group())
