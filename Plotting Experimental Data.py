import numpy as np
from matplotlib.pyplot import *
def dl():
    initial = np.array([30,35,40,45,50,55,60,65,70])
    bounce = np.array([22,26,29,34,38,40,45,50,52])

    figure(1)
    clf()

    plot(initial,bounce,"bo")
    title("Initial Height vs. Bounce Height")
    ylabel("Bounce Height")
    xlabel("Initial Height")
    a,b = np.polyfit(initial,bounce,1)
    plot(initial,a*initial + b,"r")
    show()

def fx():
    ar1 = np.loadtxt("students.txt", skiprows=1)
    half = ar1[ar1[:, 0] == 2.0]
    full = ar1[ar1[:, 0] == 1.0]
    non = ar1[ar1[:, 0] == 3.0]

    half2 = half.T
    writing = half2[3]
    mathgrade = half2[1]
    reading = half2[2]
    writing.sort()

    figure(2)
    clf()

    subplot(2, 2, 1)
    res = hist(writing, 4, color="#0033FF")
    ticks = np.array([0, 25, 50, 75, 100])
    xticks(ticks)
    title("Frequency of Writing Gr. of Half Sc. Students")

    subplot(2, 2, 2)
    plot(np.arange(1, np.size(mathgrade) + 1), mathgrade, color="red", marker="o", ls="--", label="Math")
    plot(np.arange(1, np.size(reading) + 1), reading, color="purple", marker="x", ls=":", label="Reading")
    title("Math vs Reading Gr. of Half Sc. Students")
    tight_layout()
    legend()

    subplot(2, 2, 3)
    labels = "Half", "Full", "Non"
    sizes = [55.9, 20.6, 23.5]
    explode = (0, 0, 0.1)
    pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%")
    title("Scholarship Percentages")

    subplot(2, 2, 4)
    a = reading.mean()
    ar2 = ar1.T
    b = ar2[2].mean()
    index1 = np.array(["Half-sc."])
    index2 = np.array(["All"])
    bar(index1, a, color="#CC0033")
    bar(index2, b, color="#008080")
    title("Reading Grades : Half Sc. vs All Students")
    ylabel("Average of Grades")

    show()

dl()
fx()



