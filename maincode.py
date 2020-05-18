from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import numpy as geek 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from numpy import loadtxt
import numpy as np
import pyqtgraph as pg
import pandas as pd 
import wave
from scipy.io import wavfile
from playsound import playsound
import sounddevice as sd
import soundfile as sf
from PyQt5 import QtCore, QtWidgets, QtMultimedia
#from equi_final import equalizer
import scipy.fftpack
from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from popwin import Ui_Pop
import numpy as geek 



class pop_win(QtWidgets.QMainWindow,Ui_Pop):

	def __init__(self,data_diff,data_diff_F,fs):
		super(pop_win, self).__init__()
		self.setupUi(self)
		
		self.dataX=data_diff
		self.dataY=data_diff_F
		self.fs2=fs

		self.data_line5 = self.popwindow.plotItem.plot()
		self.data_line6 = self.popwindowF.plotItem.plot()

		self.soundonbutton.clicked.connect(self.sound_on)#
		self.muteButton.clicked.connect(self.sound_OFF)#
		
		pen = pg.mkPen(color=(0, 200, 0))
		self.data_line5.setData(self.dataX,pen=pen) 
		self.data_line6.setData(self.dataY,pen=pen) 
		
		
	def sound_on(self):
		sd.play(self.dataX, self.fs2)

	def sound_OFF(self):
		sd.stop()
		
			
        

class ApplicationWindow(QtWidgets.QMainWindow):
	data3 = []
	data2= []
	data1=[]
	data4=[]
	data5=[]
	i_orig=0
	i_FF=0
	i_EF=0
	i_E=0
	i=0
	ch_orig=0
	ch_FF=0
	ch_EF=0
	ch_E=0
	value0=1
	value1=1
	value2=1
	value3=1
	value4=1
	value5=1
	value6=1
	value7=1
	value8=1
	value9=1
	value=[value0,value1,value2,value3,value4,value5,value6,value7,value8,value9]
	band=[]
	signal=[]
	#samplerate1 = []
	#out =[]

	#band1_max =0
	#band1_min =0
	
	def __init__(self):
		super(ApplicationWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.timer1 = QtCore.QTimer()
		self.timer1.setInterval(35)
		self.timer1.timeout.connect(self.update)
		self.timer1.start()

		self.data_line1 =  self.ui.orgwin.plotItem.plot()#
		self.data_line2 =  self.ui.fourer_org_win.plotItem.plot()#
		self.data_line3 =  self.ui.winEq.plotItem.plot()#
		self.data_line4 =  self.ui.winEq_FF.plotItem.plot()#

		l1=[self.ui.startbutton1,self.ui.pausebutton1,self.ui.startsong_orig,self.ui.stopm_orig,self.ui.startbuttonEq,self.ui.pausebuttonEq,
			self.ui.startsong_Eq,self.ui.stopm_Eq,self.ui.startbuttonFForig,self.ui.stopbuttonFForig,self.ui.start_FourierEq,
			self.ui.delete_FourierEq,self.ui.max]
		l2=[self.start_orig,self.pause_orig,self.song_orig,self.song_stop_1,self.start_Eq,self.pause_Eq,self.song_Eq,self.song_stop_2,
			self.start_FF_orig,self.pause_FF_orig,self.start_FF_Eq,self.pause_FF_Eq,self.popUpwindow]
		for i in range(len(l1)):
			l1[i].clicked.connect(l2[i])
#****************************************************************				
		l3=[self.ui.slider1,self.ui.slider2,self.ui.slider3,self.ui.slider4,self.ui.slider5,self.ui.slider6,self.ui.slider7,self.ui.slider8,
			self.ui.slider9,self.ui.slider10]
		l4=[lambda:self.glob(l3[0].value(),0),lambda:self.glob(l3[1].value(),1),lambda:self.glob(l3[2].value(),2),lambda:self.glob(l3[3].value(),3),
			lambda:self.glob(l3[4].value(),4),lambda:self.glob(l3[5].value(),5),
			lambda:self.glob(l3[6].value(),6),lambda:self.glob(l3[7].value(),7),lambda:self.glob(l3[8].value(),8),lambda:self.glob(l3[9].value(),9)]
		for i in range(len(l3)):

			l3[i].valueChanged[int].connect(l4[i])
#**************************************************
		l5=[self.ui.actionHamming_Window,self.ui.actionHann_Window,self.ui.actionRectangular_Window,self.ui.actionOutputOne,
			self.ui.actionOutputTwo,self.ui.actionShowResults,self.ui.actionSave,self.ui.actionOpen]
		l6=[self.Hamming,self.Hanning,self.rectangular,self.save1,self.save2,self.draw_saved,self.savefile,self.loaddata]
		for i in range(len(l5)):
			l5[i].triggered.connect(l6[i])
				
				
		

		
	########################  Functions   ############################	

	""" def onUpdate(self, host, band1_max):
		self.ui.freq1 = self.findChild(self.centralwidget)
		self.ui.freq1.setText("{}".format(self.band1_max))
 """
	def popupshow(self):
		popup = MyPopup()
		popup.show()

	def glob(self,value1,i):
		sd.stop()
		self.i=i

		self.value[i]=value1
		self.song_Eq()
	##################################################################

	def update(self):
		if(self.ch_orig):
			self.update_plot_data_orig()
		if(self.ch_FF):
			self.update_plot_data_FF_orig()
		if(self.ch_E):
			self.update_plot_data_Eq()
		
		if(self.ch_EF):
			self.update_plot_data_FF_Eq()
######################### Original #########################
	def update_plot_data_orig(self):
		pen = pg.mkPen(color=(0, 200, 0))
		#self.y_orig = self.data1[:self.i_orig] # Remove the first
		self.y_orig = self.data1 
		self.data_line1.setData(self.y_orig,pen=pen)  # Update the data.
		self.i_orig+=1

	def start_orig(self):
		
		self.ch_orig=1
		
	
	def pause_orig(self):
		self.ch_orig=0

	def song_orig(self):
		self.L=self.i_orig
		self.data2=self.data1[int(self.L):]
		sd.play(self.data2, self.fs)

	def song_stop_1(self):
		sd.stop()

######################  Equalizer ################################
	def update_plot_data_Eq(self):
		pen = pg.mkPen(color=(200, 0, 0))
				
		print("self.value=",self.value1,",self.i_E=",self.i_E)
		self.data_E1=np.fft.rfft(self.data1)
		
	
		
		self.data_E=equalizer(self.data_E1,self.value,self.i)
		self.inv=np.fft.irfft(self.data_E)
		self.data_line3.setData(self.inv, pen=pen)  # Update the data.
		
		
	def start_Eq(self):
		self.data_line3.clear()
		self.ch_E=1
	   
	def pause_Eq(self):
		self.ch_E=0
	   
	def song_Eq(self):
		self.i_EE=self.i_E
		self.dataEE=self.data_E[int(self.i_EE):]
		sd.play(self.dataEE, self.fs)

		
	def song_stop_2(self):
		sd.stop()
		

###############################  Fourier-Orig ###########################
	
	def update_plot_data_FF_orig(self):
		pen = pg.mkPen(color=(10, 50, 200))
		self.data_FF = np.fft.fft(self.y_orig)
		self.y_FF = np.abs(self.data_FF[:int(len(self.data_FF)/2)])  # Remove the first 
		self.data_line2.setData(self.y_FF, pen=pen)  # Update the data.
		self.i_FF+=1
	def start_FF_orig(self):
		self.ch_FF=1
	def pause_FF_orig(self):
		self.ch_FF=0
	

###############################  Fourier-Eq ###########################
	
	def update_plot_data_FF_Eq(self):
		pen = pg.mkPen(color=(10, 50, 200))
		self.data_FF = np.fft.fft(self.data_E)
		self.y_FF = np.abs(self.data_FF[:int(len(self.data_FF)/2)])  # Remove the first 
		self.data_line4.setData(self.y_FF, pen=pen)  # Update the data.
		self.i_EF+=1
	def start_FF_Eq(self):
		self.ch_EF=1
	def pause_FF_Eq(self):
		self.ch_EF=0
	


###########################  Max ##############################
	

        


##################################### Save ###########################

	def save1(self):
		self.ys1=self.data_E
	
	def save2(self):
		self.ys2=self.data_E

	def draw_saved(self):
		self.win = pg.GraphicsWindow()
		self.win.show()        
		p1 = self.win.addPlot()
		p1.plot(self.ys1, pen=3*0+0)
		
		p2 = self.win.addPlot()
		p2.plot(self.ys2, pen=3*0+1)

	def savefile(self):
		fileName,_ = QtGui.QFileDialog.getSaveFileName(self, 'Save File','',"All Files (*);;Wave Files (*.wav);;mpc3 Files(*.mpc3)")
		file = open(fileName,'w')
		self.saveout(fileName)
	
	
	
	def saveout(self,fileName):
		self.out= np.array(self.data_E)
		self.samplerate1 = np.array(self.fs)
		#print(self.out.shape)
		wavfile.write(fileName,self.fs, self.data_E)
			


	############################# bands ############################
	def equalizer_10band (self,data_E1,gain,x):


		self.band=[0]*10
		self.signal=[0]*len(data_E1)   
			
		for i in range(0,9):
			self.band[i] = data_E1[ int(len(data_E1)*i/10) : int(len(data_E1)*(i+1)/10)]
			if i==x :
				self.band[i] = data_E1[ int(len(data_E1)*i/10) : int(len(data_E1)*(i+1)/10)]*gain[i]
				self.signal=geek.hstack(( self.signal, self.band[i] ))

			else:
				self.signal=geek.hstack(( self.signal, self.band[i] )) 

			
			
		return self.signal,self.band

	############################# Hamming ############################

	def Hamming(self):
	
		self.data_line3.clear()
		self.data_line4.clear()

		self.freq_data = np.fft.fftfreq(len(self.data_E1))
		#self.freq_bands = np.array_split(self.freq_data ,10)
		self.freq_bands = np.linspace(0,20000, len(self.freq_data))

		self.H=[0]*10
		self.x1=[0]*10
		self.x2=[0]*10
		self.x3=[0]*10
		self.out=[0]*10
		self.Hamming_tot=[0]*10
		self.Hamm0_Inv=[0]*10
		self.ham_FF=[0]*10
		self.out1=[0]*10
		self.out2=[0]*10
		for i in range(1,8):
			min_range = int(i * 0.1* len(self.freq_bands))
			max_range = int((i+1) * 0.1 * len(self.freq_bands))
			self.H[i]=np.hamming( (max_range - min_range)*2  )
			self.x1[i] = self.freq_bands[min_range-(int(0.025*len(self.freq_bands))):min_range]
			self.x2[i]=self.freq_bands[max_range:max_range+(int(0.05*len(self.freq_bands)))]
			self.x3[i]=self.freq_bands[min_range:max_range]
			import numpy as geek
			self.out2[i] = geek.hstack((self.x3[i], self.x2[i]))
			self.out1[i] = geek.hstack((self.out2[i], self.x1[i]))  
			#self.Hamming_tot[i]=np.multiply(self.out2[i],self.out1[i][int(len(self.H[i])/4):])
			self.Hamming_tot[i]=np.multiply(self.out2[i][int(len(self.H[i])/4):],self.out1[i][int(len(self.H[i])/4):])

			self.Hamm0_Inv[i] = np.fft.irfft(self.Hamming_tot[i])
			
			self.data_line3.setData(self.Hamm0_Inv[i]) 
			self.data_line4.setData(np.abs(self.Hamming_tot[i])) 
			print("ham0")

		""" i=9
		import numpy as geek
		self.H[i]=np.hamming( int(len(self.freq_bands[i])*1.5 )  )

		self.x2[i]=self.freq_bands[i-1][int(len(self.freq_bands[i-1])*2/4): ]
		self.x3[i]=self.freq_bands[i]
		self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
		self.Hamming_tot[i]=self.out2[i] *self.H[i]
		self.Hamm0_Inv[i] = np.fft.irfft(self.Hamming_tot[i])
		  
		self.data_line3.setData(self.Hamm0_Inv[i]) 
		self.data_line4.setData(np.abs(self.Hamming_tot[i])) 
		print("ham0")


		for i in range(1,8):
			import numpy as geek

			self.x1[i]=self.freq_bands[i-1][:int(len(self.freq_bands[i-1])*2/4) ]
			self.x2[i]=self.freq_bands[i+1][int(len(self.freq_bands[i+1])*2/4): ]
			self.x3[i]=self.freq_bands[i]
			
			self.out1[i] = geek.hstack((self.x2[i], self.x3[i])) 
			self.out2[i] = geek.hstack((self.out1[i], self.x3[i])) 
			
			self.H[i]=np.hamming( int( len(self.out2[i][:(len(self.out2[i])) ] ) ))
			self.Hamming_tot[i]=self.out2[i][:(len(self.out2[i]))] *self.H[i]
			self.Hamm0_Inv[i] = np.fft.irfft(self.Hamming_tot[i])
			
			self.data_line3.setData(self.Hamm0_Inv[i]) 
			self.data_line4.setData(np.abs(self.Hamming_tot[i])) 
			print("ham0") """
	
	#########################################################################
		for i in range(1,8):
			if self.value[i] !=1 :
				self.H[i]=np.hamming( int(len(self.band[i])*2 ) )*self.value[i]
				self.x1[i]=self.band[i-1][ int(len(self.band[i-1])*2/4) : ]
				self.x2[i]=self.band[i+1][ :int(len(self.band[i+1])*2/4) ]
				self.x3[i]=self.band[i]
				import numpy as geek 
				self.out1[i] = geek.hstack((self.x1[i], self.x2[i])) 
				self.out2[i] = geek.hstack((self.out1[i], self.x3[i])) 
				self.Hamgain[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Hamgain[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Hamgain[i]+self.Hamtot[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("hamall")
		

			if self.value[0] !=1 :
				i=0
				self.H[i]=np.hamming( int(len(self.band[i])*1.5 )  )*self.value[0]
				
				self.x2[i]=self.band[i+1][ :int(len(self.band[i+1])*2/4) ]
				self.x3[i]=self.band[i]

				
				self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
				self.Hamgain[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Hamgain[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Hamgain[i]+self.Hamtot[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("ham0")

			if self.value[9] !=1 :
				i=9
				self.H[i]=np.hamming( int(len(self.band[i])*1.5 )  )*self.value[9]
				
				self.x2[i]=self.band[i-1][ :int(len(self.band[i-1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 
				self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
				self.Hamgain[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Hamgain[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Hamgain[i]+self.Hamtot[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("ham10")
		

############################# Hanning ############################

	def Hanning(self):
		
		self.data_line3.clear()
		self.data_line4.clear()
		self.H=[0]*10
		self.x1=[0]*10
		self.x2=[0]*10
		self.x3=[0]*10
		self.out=[0]*10
		self.Ham=[0]*10
		self.Hamm=[0]*10
		self.ham_FF=[0]*10
		self.out1=[0]*10
		self.out2=[0]*10
		
		for i in range(1,8):	
		
			if self.value[i] !=0 :
				self.H[i]=np.hanning( int(len(self.band[i])*2 )  )
				
				self.x1[i]=self.band[i-1][ int(len(self.band[i-1])*2/4) : ]
				self.x2[i]=self.band[i+1][ :int(len(self.band[i+1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 

				self.out1[i] = geek.hstack((self.x1[i], self.x2[i])) 
				self.out2[i] = geek.hstack((self.out1[i], self.x3[i])) 


				self.Ham[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]

				
				self.Hamm[i] = np.fft.fft(self.Ham[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Ham[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("jj")
		
		
			if self.value[0] !=0 :
				i=0
				self.H[i]=np.hanning( int(len(self.band[i])*1.5 )  )
				
				self.x2[i]=self.band[i+1][ :int(len(self.band[i+1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 
				self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
				self.Ham[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Ham[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Ham[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("jj")
		
			if self.value[9] !=0 :
				i=9
				self.H[i]=np.hanning( int(len(self.band[i])*1.5 )  )
				
				self.x2[i]=self.band[i-1][ :int(len(self.band[i-1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 
				self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
				self.Ham[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Ham[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Ham[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("jj")

			############################# rect ############################

	def rectangular(self):
		
		self.data_line3.clear()
		self.data_line4.clear()
		self.H=[0]*10
		self.x1=[0]*10
		self.x2=[0]*10
		self.x3=[0]*10
		self.out=[0]*10
		self.Ham=[0]*10
		self.Hamm=[0]*10
		self.ham_FF=[0]*10
		self.out1=[0]*10
		self.out2=[0]*10
		
		for i in range(1,8):	
		
			if self.value[i] !=0 :
				self.H[i]=scipy.signal.boxcar( int(len(self.band[i])*2 )  )
				
				self.x1[i]=self.band[i-1][ int(len(self.band[i-1])*2/4) : ]
				self.x2[i]=self.band[i+1][ :int(len(self.band[i+1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 

				self.out1[i] = geek.hstack((self.x1[i], self.x2[i])) 
				self.out2[i] = geek.hstack((self.out1[i], self.x3[i])) 


				self.Ham[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]

				
				self.Hamm[i] = np.fft.fft(self.Ham[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Ham[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("jj")
		
		
			if self.value[0] !=0 :
				i=0
				self.H[i]=scipy.signal.boxcar( int(len(self.band[i])*1.5 )  )
				
				self.x2[i]=self.band[i+1][ :int(len(self.band[i+1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 
				self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
				self.Ham[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Ham[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Ham[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("jj")
		
			if self.value[9] !=0 :
				i=9
				self.H[i]=scipy.signal.boxcar( int(len(self.band[i])*1.5 )  )
				
				self.x2[i]=self.band[i-1][ :int(len(self.band[i-1])*2/4) ]
				self.x3[i]=self.band[i]

				import numpy as geek 
				self.out2[i] = geek.hstack((self.x2[i], self.x3[i])) 
				self.Ham[i]=self.out2[i] [ : (len(self.out2[i])) ]*self.H[i]
				self.Hamm[i] = np.fft.fft(self.Ham[i])
				self.ham_FF[i] = np.abs(self.Hamm[i][:int(len(self.Hamm[i])/2)])  
				self.data_line3.setData(self.Ham[i]) 
				self.data_line4.setData(np.abs(self.ham_FF[i])) 
				print("jj")
				
		


############################################################################
	def loaddata(self):
		filename = QFileDialog.getOpenFileName(self)
		if filename[0]:
			if filename[0].endswith('.wav'):
				#filename = QFileDialog.getOpenFileName()
				path3 = filename[0]
	    
				self.MyBrowse = path3
				self.storedata1(path3)
				



	def storedata1(self, path):
		data1, fs = sf.read(path, dtype='float32') 
		
		self.data1 = np.mean(data1, axis=1)
		self.data1 = self.data1[ :int(len(self.data1)/12) ]
		self.data5 = np.array(self.data1)
		self.fs=fs
		#print(len(self.data1))
		#print(self.data5.shape)
	
	def popUpwindow(self):

		global application1
		self.diff=self.data1-self.data_E
		self.datax = np.fft.fft(self.diff)
		self.datax2 = np.abs(self.datax[:int(len(self.datax)/2)])  # Remove the first 
		
		application1=pop_win(self.diff,self.datax2,self.fs)
		application1.show()




def main():
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()

	application.show()
	app.exec_()


if __name__ == "__main__":
	main()
