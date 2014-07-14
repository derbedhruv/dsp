# this file shall just read in shit form a file name, specified in the start
# modify the shat out of it yo
# by Jesse Pinkman

fileName = "20140522-0002_1.txt"		# enter the file name, bitch
x = [] 
y = []			# shall store the data. Don't mess with this, bitch
headerLines = 3		# enter the numberof header lines, bitch

f = open(fileName, 'r')		# gonna open the file for reading, bitch. f is a 'file' object

# rawdata = f.readlines()		# just puttin' that data into a nice string object yo

dataChopped = f.read().split('\n')	# now we have a list of the data line by line. feel good, bitch

# now pay attention. Next we split the shitout of this, avoiding header lines.
for i in range(headerLines, len(dataChopped)-1):
  m,n = dataChopped[i].split('\t')		# split shall give a list/tuple. THis needs to be read into 2 seperate variables or however many variables you have
  x.append(float(m))
  y.append(float(n))
  
# That's it. The file has now been read into 2 variables for ya. Now you can do interesting shit with it.
# I am going to implement a DC removal filter now, asshole.

import scipy.signal as signal
from pylab import *

# some function definitions which were taken from http://mpastell.com/2010/01/18/fir-with-scipy/
#Plot frequency and phase response
def mfreqz(b,a=1):
    w,h = signal.freqz(b,a)
    h_dB = 20 * log10 (abs(h))
    subplot(211)
    plot(w/max(w),h_dB)
    ylim(-150, 5)
    ylabel('Magnitude (db)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Frequency response')
    subplot(212)
    h_Phase = unwrap(arctan2(imag(h),real(h)))
    plot(w/max(w),h_Phase)
    ylabel('Phase (radians)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Phase response')
    subplots_adjust(hspace=0.5)

#Plot step and impulse response
def impz(b,a=1):
    l = len(b)
    impulse = repeat(0.,l); impulse[0] =1.
    x = arange(0,l)
    response = signal.lfilter(b,a,impulse)
    subplot(211)
    stem(x, response)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Impulse response')
    subplot(212)
    step = cumsum(response)
    stem(x, step)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Step response')
    subplots_adjust(hspace=0.5)

# the following lines have just been kept as a test artificial case, uncomment as needed..
'''
x = arange(0,10, 1/(2*nyquistF))
y = sin(2*pi*100*x) + 0.5
'''

# defining a highpass filter yo..
# write the cutoff seperately bitch
cutOff = 0.1		# the cutoff frequency, in the same units as the following nyquist frequency
nyquistF = 2500.0	# the nyqwuist frequency
n = 5001		# window length, larger one makes a sharper filter
plotPoints = len(x)	# number of points to plot yo
unplotPoints = n	# number of points to ignore at the start, weird filter feature

a = signal.firwin(n, cutoff=cutOff, window="hamming", nyq=nyquistF)


# the following converts lowpass to highpass yo
a = -a
a[n/2] = a[n/2] + 1
# mfreqz(a)

filtered = signal.lfilter(a, 1, y) + y[0]

# spectrum1 = fft(y)

# plot(log10(abs(spectrum1)))
plot(x[unplotPoints:plotPoints], y[unplotPoints:plotPoints], 'g')
plot(x[unplotPoints:plotPoints], filtered[unplotPoints:plotPoints], 'b')
show()


