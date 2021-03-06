import scipy
import matplotlib.colors
import os
import sys
import inspect
import matplotlib.pyplot as plt

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
gsdict = {'thermal':0,
          'thermal2':1,
          'thermal3':2,
          'bright':3,
          'copper2':4,
          'dusk':5,
          'earth':6,
          'hicontrast':7,
          'pastel':8,
          'pink2':9,
          'sepia':10,
          'cold':11,
          'RoyalGold':12,
          'FCPM_001':13,
          'CMR':14}


def loadct(num, r=False, mayavi=False, **kwargs):
    if not mayavi:

        output = scipy.genfromtxt(cmd_folder+'/idl_colors.txt',
                                  skip_header=256*num,
                                  skip_footer=(39-num)*256)/255.
        if r:
            output = output[::-1]
            
        return matplotlib.colors.LinearSegmentedColormap.from_list('idl', output, **kwargs)
    else:
        output = scipy.ones((256,4),dtype=int)
        output[:,0:3] = scipy.genfromtxt(cmd_folder+'/idl_colors.txt',
                                         skip_header=256*num,
                                         skip_footer=(39-num)*256,dtype=int)
        if r:
            output = output[::-1]

        return output

def loadgs(num, r=False, mayavi=False, **kwargs):
    if isinstance(num,str):
        name = num
        if name.endswith('_r'):

            r = True
            num = gsdict[num[:-2]]
        else:
            num = gsdict[num]
 
    else:
        name = 'gs'
    
    if not mayavi:

        output = scipy.genfromtxt(cmd_folder+'/gs_colors.txt',
                                  skip_header=256*num,
                                  skip_footer=(14-num)*256)
        if r:
            output = output[::-1]
            
        return matplotlib.colors.LinearSegmentedColormap.from_list(name, output,**kwargs)
    else:
        output = scipy.ones((256,4),dtype=int)
        output[:,0:3] = scipy.genfromtxt(cmd_folder+'/gs_colors.txt',
                                         skip_header=256*num,
                                         skip_footer=(14-num)*256,dtype=int)
        if r:
            output = output[::-1]

        return output

def showct():
    a=scipy.outer(scipy.arange(0,1,0.01),scipy.ones(10))
    plt.figure(figsize=(10,5))
    plt.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
    l=56
    idx = 0
    for m in xrange(40):
        plt.subplot(1,l,idx+1)
        idx += 1
        plt.axis("off")
        plt.imshow(a,aspect='auto',cmap=loadct(m),origin="lower")
        plt.title('idl'+str(m),rotation=90,fontsize=10)

    for m in xrange(15):
        plt.subplot(1,l,idx+1)
        idx += 1
        plt.axis("off")
        plt.imshow(a,aspect='auto',cmap=loadgs(m),origin="lower")
        plt.title('gs'+str(m),rotation=90,fontsize=10)

    plt.show()
