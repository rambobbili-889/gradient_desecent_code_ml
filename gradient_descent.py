'''
This code used to implement the gradient_descent_method in ML
'''

import numpy as np
import sys

class GRADIENT_DESCENT:
    def __init__(self):
        try:
            self.x_train = np.array([1, 2, 3, 4, 5])
            self.y_train = np.array([5, 7, 9, 11, 13])
            self.m_value = 0
            self.c_value = 0
            self.learning_rate = 0.04
            self.iteration = 100
            self.no_of_rows = len(self.x_train)
        except Exception as e:
            error_type, error_message, error_line_no = sys.exc_info()
            print(error_type, error_message, error_line_no.tb_lineno)

    def formula(self):
        try:
            for i in range(self.iteration):
                self.y_train_predict = self.m_value * self.x_train + self.c_value
                self.cost_function = (1/self.no_of_rows)*sum([i**2 for i in (self.y_train - self.y_train_predict)])
                self.m_derivative = -(2/self.no_of_rows) * sum(self.x_train * (self.y_train-self.y_train_predict))
                self.c_derivative = -(2/self.no_of_rows) * sum(self.y_train - self.y_train_predict)
                self.m_value = self.m_value - self.learning_rate * self.m_derivative
                self.c_value = self.c_value - self.learning_rate * self.c_derivative
                print(f'M_Value : {self.m_value} , C_value : {self.c_value} , Loss : {self.cost_function}, {i}')
        except Exception as e:
            error_type, error_message, error_line_no = sys.exc_info()
            print(error_type, error_message, error_line_no.tb_lineno)

if __name__ == "__main__":
    try:

        obj = GRADIENT_DESCENT()
        obj.formula()
    except Exception as e:
        error_type, error_message, error_line_no = sys.exc_info()
        print(error_type, error_message, error_line_no.tb_lineno)