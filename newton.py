import timeit
def f(x):
  return x**4-2*x**3-5
def df(x):
  return 4*x**3-6*x**2
starttime=timeit.default_timer()
print("Start time:",starttime)
x0=1

tolerance=1e-6
max_iterations=100
for i in range(max_iterations):
  fx=f(x0)
  dfx=df(x0)
  x1=x0-fx/dfx
  if abs(fx)<tolerance:
    print(f"Root found at x = {x1:.6f}")
    break
  else:
    x0=x1
print("Time taken: ",timeit.default_timer()-starttime)
