from contextlib import contextmanager
from time import time, sleep

'''
1. Дан класс:
    class Lock(object):
      def __init__(self):
        self.lock = False
    
    Сделать менеджер контекста, который может переопределить 
    значение lock на True внутри блока контекста.
'''

@contextmanager
def de_lock(some_lock_var):
	some_lock_var.lock=True
	yield some_lock_var


class Lock(object):
      def __init__(self):
        self.lock = False

'''
+2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные 
   в теле и писал их в консоль, пример использования:
    
    with no_exceptions():
      1 / 0 # => logs: ZeroDivisionError

    print('Done!') # => continues execution
'''
@contextmanager
def exception_catcher():
	try:
		yield
	except Exception as e:
		print('Error. Exception is {}'.format(str(e)))

'''
+3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, 
   пример использования:
    
    with TimeIt() as t:
      some_long_function()

    print('Execution time was:', t.time) 
'''
@contextmanager
def speedometer():
	start=time()
	sleep(1)
	end=time()
	result=end-start
	yield 
	print('{} seconds taked to do this function'.format(result))

if __name__=='__main__':
	def some_function(a,b):
		return (a+b)*100
	print('Task 1: ')
	new_lock=Lock()
	print('Сейчас значение lock - {}'.format(new_lock.lock))
	with de_lock(new_lock):
		print('Теперь значение lock - {}'.format(new_lock.lock))
	print('***************************************************')
	print('Task 2: ')
	with exception_catcher():
		1/0
	with exception_catcher():
		abc+=1
	print('***************************************************')
	print('Task 3: ')
	with speedometer():
		print('The result of function activity is ', some_function(3,5))
	print('***************************************************')