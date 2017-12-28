epsilon = 1e10
max_iter = 1000
def calc_pi(epsilon, max_iter):
    pi = 3
    prev_pi = 0
    s = 1
    for i in range(2,max_iter,2):
        pi = pi + s * (4. / (i * (i + 1) * (i + 2)))
        s = -s
        if abs(pi - prev_pi) < epsilon:
            return pi
        prev_pi = pi
    return None
pi = calc_pi(epsilon, max_iter)