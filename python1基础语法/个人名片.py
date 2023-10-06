# 姓名 公司 职位 电话 邮箱
name = input('请输入你的姓名：')
company = input('请输入你所在的公司：')
position = input('请输入你的职位：')
number = input('请输入你的电话')
post = input('请输入你的邮箱:')

print(company)
print('%s(%s)' % (name, position))
print('电话：%s' % number)
print('邮箱：%s' % post)