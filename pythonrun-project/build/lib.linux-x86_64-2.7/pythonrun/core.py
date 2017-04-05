def get_message():
    return "Successful run - congratulations"


def print_message():
    print get_message()


class Basical:
	def __init__(self,n):
		self.numb = n 
	def out(self):
		print (self.numb)


class ThirdTurn(Basical):

	def plus(self, k):
		self.numb += k

		if k >= 6:
			print("Полученное число больше 6 - Угадайте производные?")
		else:
			print("Полученое число меньше 6 - Угадайте производные?")
		pass


obj3 = ThirdTurn(input("Введите число для вывода: "))
obj3.plus(6)
obj3.out()