import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 1, 2**(1/2), 3**(1/2), 4**(1/2), 5**(1/2), 6**(1/2), 7**(1/2), 8**(1/2), 9**(1/2), 10**(1/2)]

plt.plot(x,y, color = 'red')
ay = plt.gca()
ax = plt.gca()
ay.set_ylim(0,5)
ax.set_xlim(0,10)
plt.grid(True)
plt.title('y=sqrt(x)')
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))
plt.show()