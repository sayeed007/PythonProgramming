import matplotlib

print("Matplotlib Version:",matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

'''
#Two point Joining
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, "o")
plt.show()

#Multipoint Joining
xpoints = np.array([1, 2, 3, 4])
ypoints = np.array([1, 2, 6, 8])

#plt.plot(xpoints, ypoints, marker="o-" , ms = 20) #ms = MarkerSize || mec = MerkerColor || mfc = MarkerFaceColor || c = color || lw = LineWidth
plt.plot(ypoints, 'o', ms = 5, mec = 'r', mfc = 'm', linestyle='dotted', c = '#4CAF50', lw = '10' ) 
plt.plot(xpoints, 'o', ms = 5, mec = 'r', mfc = 'm', linestyle='dotted', c = '#4CAF50', lw = '10' )

#"'or' => red || 'og' => green also available b=blue,c,m,y,k= black,w"
#"'o-' => solid line || 'o:' => doted line || 'o--' => dashed line || 'o-.' => dashed/dot                 line ||"
#marker can be 
"o" => Circlr       "*" => Star                 '.'	=> Point	
',' => Pixel	    'x' => X	                'X' => X (filled)	
'+'	=> Plus	        'P'	=> Plus (filled)	    's'	=> Square	
'D'	=> Diamond	    'd'	=> Diamond (thin)	    'p'	=>Pentagon	
'H'	=> Hexagon	    'h'	=> Hexagon	            'v'	=>Triangle Down	
'^'	=> Triangle Up	'<'	=> Triangle Left	    '>'	=> Triangle Right	
'1'	=> Tri Down	    '2'	=> Tri Up	            '3'	=> Tri Left	
'4'	=> Tri Right	'|'	=> Vline	            '_'	=> Hline

plt.show()
'''

#Multiple Lines
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

#Setting Font Properties for Title & label
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Adding Title for plot
plt.title("Sports Watch Data", fontdict = font1, loc='left') # right / center

#Labeling X & Y axis
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)


plt.plot(x, y, "o--")
#Ploting Grid
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
#(axis = 'x') => brings only x axis grid 
plt.show()