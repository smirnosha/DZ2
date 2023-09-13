from cvxopt.modeling import variable, op
import time

start = time.time()
x = variable(2, 'x')
z = -(x[0] + 2 * x[1])  # Функция цели

mass1 = x[0] + 2 * x[1] <= 6
mass2 = 2 * x[0] + x[1] <= 8
mass3 = x[1] <= 2
x_non_negative = (x >= 0) #"3"
problem = op(z, [mass1, mass2, mass3, x_non_negative])
problem.solve(solver='glpk')

problem.status
print("Прибыль:")
print(abs(problem.objective.value()[0]))
print("Результат:")
print(x.value)
stop = time.time()
print("Время :")
print(stop - start)
