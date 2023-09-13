from scipy.optimize import linprog
import time
start = time.time()
c = [-1,-2] #Функция цели
A_ub = [[1,2]] #'1'
b_ub = [6]#'1'
A_eq = [[2,1]] #'2'
b_eq = [8] #'2'
A_ac = [[0,2]] #'2'
b_ac = [2] #'2'
A_av = [[1,1]] #'2'
b_av = [0] #'2'
print (linprog(c, A_ub, b_ub, A_eq, b_eq))
stop = time.time()
print ("Время :")
print(stop - start)

