from scipy.stats import truncnorm
import numpy as np 
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
X = get_truncated_normal(mean=8, sd=2, low=1, upp=100)

a = X.rvs(10)
print(a)
print(np.random.choice(a,10, replace=False))
print(np.random.choice(a,10, replace=True))

def random_floats(low, high, size):
    return [np.random.uniform(low, high) for _ in range(size)]
b = random_floats(0.5, 2.8, 5)
print(b)
print(np.random.choice(b,5, replace=False))