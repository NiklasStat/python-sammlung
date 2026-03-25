from collections import Counter
import matplotlib.pyplot as plt
import math
from statistics import variance
import random
import numpy as np



num_friends = [2, 3, 4, 3, 4, 5, 3, 4, 3, 6, 3, 5, 4, 6, 4, 9, 3, 5, 4, 11, 14, 12, 12, 11, 14, 21, 21, 24, 15, 14, 18, 10, 8, 22]
friend_counts = Counter(num_friends)
print(friend_counts)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))  # 2x3 Raster



xs = range(25)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 25, 0, 10])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

laenge, maxi, mini, kleinste, groesste = len(num_friends), max(num_friends), min(num_friends), sorted(num_friends)[0], sorted(num_friends)[-1]
print(laenge, maxi, mini, kleinste, groesste)

def mean(x):
    return sum(x)/len(x)

print(mean(num_friends))

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(median(num_friends))

def mode(x):
    counts = Counter(x)
    print(counts)
    max_count = max(counts.values())
    print(max_count)
    print("_____________")
    print(counts.keys())
    print(counts.values())
    print(counts.items())
    print("____________")
    return [x_i for x_i, count in counts.items()
    if count == max_count]

print(mode(num_friends))

def standard_deviation(x):
    return math.sqrt(variance(x))
print(standard_deviation(num_friends))

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend(loc=4) # bottom right
plt.title("Various Normal cdfs")
plt.show()

print("________")
# find approximate inverse using binary search
# if not standard, compute standard and rescale
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1 # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there
        if mid_p < p:
    # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
    # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

print(inverse_normal_cdf(0.6, mu=0, sigma=1, tolerance=0.00001))

print("_________--------")
print(random.random())
print(random.random())
print(random.random())

def bernoulli_trial(p):
    return 1 if random.random() < p else 0
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

print("NNNNNNNNNNNNNNNNNNNN")
print(binomial(10, 0.3))


def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
 # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
    [v / num_points for v in histogram.values()],
     0.8,
    color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
 # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
    for i in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()

make_hist(0.4, 10, 100)





# Klassenintervalle und Wahrscheinlichkeiten
intervals = [0, 10, 30, 50, 100]
probabilities = [0.1, 0.2, 0.3, 0.4]

# Berechnung der Höhen (Höhe = Fläche / Breite des Intervalls)
widths = [intervals[i+1] - intervals[i] for i in range(len(intervals)-1)]
heights = [prob / width for prob, width in zip(probabilities, widths)]

# Median-Wert
def median_neu(Intervall, Wahrscheinlichkeiten):
    k = 0
    PR_u = 0
    PR_o = 0
    oben = []

    while PR_o < 0.5:
        PR_u = sum(Wahrscheinlichkeiten[:(k-1)])
        PR_o = sum(Wahrscheinlichkeiten[:k])
        print(PR_o)
        if PR_o > 0.5:
            oben = [k-1, Intervall[k]]
            unten = [k-2, Intervall[k-1]]
            median = Intervall[k-1] + (Intervall[k]-Intervall[k-1])*(0.5-PR_u)/(PR_o-PR_u)
            print(unten, oben, PR_u, PR_o)
            return round(median, 2)
        k += 1

median = median_neu(intervals, probabilities)


# Histogramm zeichnen
plt.bar(intervals[:-1], heights, width=widths, align='edge', edgecolor='black', alpha=0.7)

# Wahrscheinlichkeiten in die Balken schreiben
for i in range(len(heights)):
    x_position = intervals[i] + widths[i] / 2  # Mittelpunkt des Balkens
    plt.text(x_position, heights[i] / 2, f"{probabilities[i]:.1f}", ha='center', va='center', color='black', fontsize=10)

# Klassenintervalle unter die x-Achse schreiben
plt.xticks(intervals, labels=[f"{intervals[i]}" for i in range(len(intervals))])

# Median als gestrichelte Linie einzeichnen
plt.axvline(x=median, color='red', linestyle='--', linewidth=2, label=f'Median = {median}')
plt.legend()

# Achsentitel und Beschriftungen
plt.xlabel('Intervalle')
plt.ylabel('Höhe (Dichte)')
plt.title('Histogramm mit Median als gestrichelte Linie')

# Zeige das Diagramm
plt.show()








