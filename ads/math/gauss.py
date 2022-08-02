import matplotlib.pyplot as plt
import numpy as np
import math

def trick(n:int) -> int:
  """Sum of series of integers from 0 up to :n:
  Also known as Gauss Summation or Gauss Trick
  
  n = 10
  1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = ?
  (1 + 10) + (2 + 9) + (3 + 8) + (4 + 7) + (5 + 6) = ?
  (11) + (11) + (11) + (11) + (11) = ?
  which is equal to: (10 * (11)) // 2
  """
  return (n * (n + 1)) // 2

def distribution(x: float, mu:float = 0.0, sigma:float = 1.0) -> float:
  """Plot Gaussian.
  Used in statistics.
  https://en.wikipedia.org/wiki/Normal_distribution
  """
  z = 1./sigma * math.sqrt(2*math.pi)
  return z*pow(math.e, -(x-mu)**2/(2*sigma*sigma))

def plot_distribution() -> None:
  X = np.arange(-5, 5, .1)
  Y1 = list(map(lambda x: distribution(x), X))
  Y2 = list(map(lambda x: distribution(x, 2, 1), X))
  plt.plot(X, Y1)
  plt.bar(X, Y1)
  plt.show()


if __name__ == "__main__":
  print(trick(100))
  print(distribution(24))
  print(distribution(1,4,2))
  plot_distribution()
