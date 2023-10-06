# eval将字符串当成有效的表达式来求值,安全风险很大，不要用eval处理前端传递过来的内容
print(eval("1+1"))
print(type(eval("[1,2,3,4,5]")))
