#!/usr/bin/python3
import sys
import argparse
import re
import utils as utils
from Parser import parsing, ft_return_error, ft_parse_token, ft_get_sign, ft_merge_sign, ft_get_max_degree, ft_calcul_side 
from solver_3rd import solver_3rd

class computer:
    A = 0
    B = 0
    C = 0
    Z = 0
    sign = 1
    DELTA = 0
    degre = 0

    def __init__(self,token):
        for tok in token:
            # print(tok)
            if tok[1] == 0:
                self.C += tok[0]
            elif tok[1] == 1:
                self.B += tok[0]
            elif tok[1] == 2:
                self.A += tok[0]
            elif tok[1] == 3:
                self.Z += tok[0]
        self.finding_degre()
        self.solving_equation()

    def solving_equation(self):
        self.print_reduction()
        if self.degre == 3:
            solver_3rd(self.Z,self.A,self.B,self.C)
        elif self.degre == 2:
            self.solve_2_degre() 
        elif self.degre == 1:
            self.solve_1_degre()
        elif self.degre == 0:
            self.solve_0_degre()

    def print_reduction(self):
        # print  ("Z = " + str(self.Z))
        # print  ("A = " + str(self.A))
        # print  ("B = " + str(self.B))
        # print  ("C = " + str(self.C))
        print("degre: ",self.degre)
        print("Simplified form: ", end="")
        if self.C != 0:
            if self.C < 0:
                utils.print_sign(self.C)
            utils.print_abs(self.C)
        if self.B != 0:
            utils.print_sign(self.B)
            utils.print_abs(self.B)
            print(" * X ",end="")
        if self.A != 0:
            utils.print_sign(self.A)
            utils.print_abs(self.A)
            print(" * X^2 ",end="")
        if self.Z != 0:
            utils.print_sign(self.Z)
            utils.print_abs(self.Z)
            print(" * X^3 ",end="")
        print("= 0")

    def finding_degre(self):
        if self.Z != 0:
            self.degre = 3
        elif self.A != 0:
            self.degre = 2
        elif self.B != 0:
            self.degre = 1
        else:
            self.degre = 0

    def solve_2_degre(self):
        self.DELTA = self.B**2 - 4*self.A*self.C
        print ("DELTA =" + str(self.DELTA))
        if self.DELTA == 0:
            X = -self.B / 2 * self.A
            print ("This polynomial equation have 1 solution:\n X = " + str(X))
        elif self.DELTA > 0:
            print("This polynomial equation have 2 solution:")
            print("X1 = " + str(-self.B) + " + square(" + str(self.DELTA) + ") / " + str(2 * self.A))
            print("X2= " + str(-self.B) + " - square(" + str(self.DELTA) + ") / " + str(2* self.A))
            X1 = (-self.B + utils.Sqrt(self.DELTA)) / 2 * self.A
            X2 = (-self.B - utils.Sqrt(self.DELTA)) / 2 * self.A
            print ("X1 = " + str(X1) + " X2 = " + str(X2))
        elif self.DELTA < 0:
            print("This polynomial equation have 2 complex solution:")
            print("X1 = " + str(-self.B) + "/" + str(2* self.A) + " - i * square(" + str(-self.DELTA) + ")/" + str(2* self.A))
            print("X2= " + str(-self.B) + "/" + str(2* self.A) + " + i * square(" + str(-self.DELTA) + ")/" + str(2* self.A))
            X1 = -self.B / 2 * self.A
            X2 = -self.B / 2 * self.A
            I1 = (utils.Sqrt(-self.DELTA)) / 2 * self.A
            I2 = (utils.Sqrt(-self.DELTA)) / 2 * self.A
            print ("X1 = " + str(X1) + " + " + str(I1) + " * i")
            print ("X2 = " + str(X2) + " - " + str(I2) + " * i")

    def solve_1_degre(self):
        if self.B != 0:
                X = -self.C / self.B  
                print ("This equation have one solution:\nX= " + str(-self.C) + "/" + str(self.B) + "\nX= " + str(X))
        elif self.B == 0.0 and self.C != 0.0:
                sys.exit("This equation is wrong")

    def solve_0_degre(self):
        if self.C == 0.0:
                print ("Every Number are solution")
        else:
                print ("There is no solution and the result is absurd")	

    def Add(self, i, sign, s):
        V = 0
        tmp = i.split('*')
        if tmp[0].find(s) == -1:
            V += float(tmp[0]) * sign
        elif tmp[0].find("-") == -1:
            V += 1.0 * sign
        else:
            V += -1.0 * sign
        return(V)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a polinomial equation')
    parser.add_argument("equation", help="enter an unique string as the the equation")
    args = parser.parse_args()
    raw_str = args.equation
    splitted = raw_str.split("=")
    token = parsing(splitted)
    # print("token: ",token)
    computer(token)
