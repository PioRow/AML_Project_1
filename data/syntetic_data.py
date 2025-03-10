import numpy as np

def generate_data(p,n,d,g, seed=None):
    if seed is not None:
        np.random.seed(seed)
    y=np.random.binomial(1,p,n)
    cov=np.eye(d)
    for i in range(d):
        for j in range(d):
            cov[i,j]=g**abs(i-j)
    X=np.ndarray((n,d))
    for i in range(n):
        X[i,:]=np.random.multivariate_normal(np.zeros(d),cov) if y[i]==0 \
            else np.random.multivariate_normal(np.ones(d)/d,cov)
    return X, y
x,y=generate_data(0.5, 100, 10, 0.5, seed=0)

