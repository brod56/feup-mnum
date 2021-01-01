import math


def jacobian(df1x, df1y, df2x, df2y, x, y):
    return df1x(x, y) * df2y(x, y) - df1y(x, y) * df2x(x, y)

def do_converge(dg1x, dg1y, dg2x, dg2y, guess_x, guess_y): # should check this before applying newton/picard to system
    return abs(dg1x(guess_x,guess_y)) + abs(dg2x(guess_x,guess_y)) < 1 and abs(dg1y(guess_x,guess_y)) + abs(dg2y(guess_x,guess_y)) < 1


def newton_null_at_guess(f, df, guess, error):
    while abs(f(guess)) > error:
        guess -= f(guess) / df(guess)
    return guess


def newton_max_iterations(f, df, guess, max_iter):
    for i in range(max_iter):
        guess -= f(guess) / df(guess)
    return guess


def picard_peano_max_iterations(g, guess, max_iter):  # f(x) = 0 <-> x = g(x)
    for i in range(max_iter):
        guess = g(guess)
    return guess


def newton_2var_max_iterations(f1, f2, df1x, df1y, df2x, df2y, guess_x, guess_y, max_iter):
    for i in range(max_iter):
        guess_x -= (f1(guess_x, guess_y) * df2y(guess_x, guess_y) - df1y(guess_x, guess_y) * f2(guess_x, guess_y)) / jacobian(guess_x, guess_y)
        guess_y -= (df1x(guess_x, guess_y) * f2(guess_x, guess_y) - df2x(guess_x, guess_y) * f1(guess_x, guess_y)) / jacobian(guess_x, guess_y)
    return guess_x, guess_y


def picard_peano_2var_max_iterations(g1, g2, guess_x, guess_y, max_iter):  # y = g1(x,y) with f1, x = g2(x,y) with f2
    for i in range(max_iter):
        guess_x = g1(guess_x)
        guess_y = g2(guess_y)
    return guess_x, guess_y

