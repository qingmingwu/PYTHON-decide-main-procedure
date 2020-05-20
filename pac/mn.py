# 主程序运行 - 理解为就是当前文件中运行代码，我的是sublime 编辑器，所以直接快捷键ctrl+b即可云心主程序


def print_print():
	print("__name__ : ", __name__)

# 打印__name__，结果为：__name__ :  __main__
print_print()



# 总结：
# 	主程序运行__name__ = "__main__"
# 	导入模式运行__name__ = "mn" -> 主程序文件名称

# 所以用: if __name__ == "__main__":
# 			app.run() # 这个只是应用示例
