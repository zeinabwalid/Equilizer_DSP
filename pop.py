from PyQt5 import QtWidgets
from seven import Ui_MainWindow
from popwin import Ui_Pop
from equalizer import equalizer_10band
import sys
import os
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
application = None
application1 = None

import scipy.fftpack

class pop_win(QtWidgets.QMainWindow,Ui_Pop):

	def __init__(self):
		super(pop_win, self).__init__()
	    self.setupUi(self)
		self.data_line5 = self.popwindow.plotItem.plot()
		self.data_line6 = self.popwindowF.plotItem.plot()

		#self.soundonbutton.clicked.connect(application.asm fun sot)
		#self.muteButton.clicked.connect(application.asm fun mute)


class ApplicationWindow(QtWidgets.QMainWindow,Ui_MainWindow ):
	#data2 = pd.read_csv('data.csv')
	data3 = []
	data2= []
	data1=[]
	data4=[]
	
	i_orig=0
	i_FF=0
	i_EF=0
	i_E=0
	ch_orig=0
	ch_FF=0
	ch_EF=0
	ch_E=0
	value1=0
	value2=0
	value3=0
	value4=0
	value5=0
	value6=0
	value7=0
	value8=0
	value9=0
	value10=0
	def __init__(self):
		super(ApplicationWindow, self).__init__()
		self.setupUi(self)
		
		#self.setupUi(self)
				
		self.timer1 = QtCore.QTimer()
		self.timer1.setInterval(35)
		self.timer1.timeout.connect(self.update)
		self.timer1.start()

		self.data_line1 =  self.orgwin.plotItem.plot()#
		self.data_line2 =  self.fourer_org_win.plotItem.plot()#
		self.data_line3 =  self.winEq.plotItem.plot()#
		self.data_line4 =  self.winEq_FF.plotItem.plot()#
				
		self.startbutton1.clicked.connect(self.start_orig)#
		self.pausebutton1.clicked.connect(self.pause_orig)#
		self.startsong_orig.clicked.connect(self.song_orig)#
		self.stopm_orig.clicked.connect(self.song_stop_1)#

		self.startbuttonEq.clicked.connect(self.start_Eq)#
		self.pausebuttonEq.clicked.connect(self.pause_Eq)#
		self.startsong_Eq.clicked.connect(self.song_Eq)#
		self.stopm_Eq.clicked.connect(self.song_stop_2)#

		self.startbuttonFForig.clicked.connect(self.start_FF_orig)#
		self.stopbuttonFForig.clicked.connect(self.pause_FF_orig)#

		self.start_FourierEq.clicked.connect(self.start_FF_Eq)#
		self.delete_FourierEq.clicked.connect(self.pause_FF_Eq)#

#		self.popwinbutton.clicked.connect(self.popUpwindow)

		self.slider1.valueChanged[int].connect(self.glob1)#
		self.slider2.valueChanged[int].connect(self.glob2)#
		self.slider3.valueChanged[int].connect(self.glob3)#
		self.slider4.valueChanged[int].connect(self.glob4)#
		self.slider5.valueChanged[int].connect(self.glob5)#
		self.slider6.valueChanged[int].connect(self.glob6)#
		self.slider7.valueChanged[int].connect(self.glob7)#
		self.slider8.valueChanged[int].connect(self.glob8)#
		self.slider9.valueChanged[int].connect(self.glob9)#
		self.slider10.valueChanged[int].connect(self.glob10)#

		self.max.clicked.connect(self.popUpwindow)
	
		#self.max.clicked.connect(self.max)#
		self.Ham.clicked.connect(self.Hamming)#

		self.save1.clicked.connect(self.save1)
		self.save2.clicked.connect(self.save2)
		self.saved.clicked.connect(self.draw_saved)
		self.Ham.clicked.connect(self.Hamming)
		
		self.actionSave.triggered.connect(self.savefile)		
		
	########################  Functions   ############################	
	def glob1(self,value):
		sd.stop()
		self.value1=value
		self.song_Eq()
	def glob2(self,value):
		sd.stop()
		self.value2=value
		self.song_Eq()
	def glob3(self,value):
		sd.stop()
		self.value3=value
		self.song_Eq()
	def glob4(self,value):
		sd.stop()
		self.value4=value
		self.song_Eq()
	def glob5(self,value):
		sd.stop()
		self.value5=value
		self.song_Eq()
	def glob6(self,value):
		sd.stop()
		self.value6=value
		self.song_Eq()	
	def glob7(self,value):
		sd.stop()
		self.value7=value
		self.song_Eq()	
	def glob8(self,value):
		sd.stop()
		self.value8=value
		self.song_Eq()	
	def glob9(self,value):
		sd.stop()
		self.value9=value
		self.song_Eq()	
	def glob10(self,value):
		sd.stop()
		self.value10=value
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
				
		self.data_E1=np.fft.fft(self.data1)
		self.data_E2=np.abs(self.data_E1)
	    
		mina=np.amin(self.data_E2)
		maxa=np.amax(self.data_E2)
		
		self.data_E,self.band1,self.band2,self.band3,self.band4,self.band5,self.band6,self.band7,self.band8,self.band9,self.band10=equalizer_10band(mina,maxa,self.data1,self.fs, self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,self.value7,self.value8,self.value9,self.value10)
	
		#self.y_E=self.data_E[:self.i_E]
		self.data_line3.setData(self.data_E, pen=pen)  # Update the data.
		self.i_E+=1
		
	def start_Eq(self):
		self.data_line2.clear()
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
	
	def diff(self):
		self.data_line5=self.data1-self.data_E
		self.y1_FF = np.fft.fft(self.data_line5)
		self.data_line6 = np.abs(self.y1_FF[:int(len(self.y1_FF)/2)]) 

		
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
		self.out= np.array(self.data1)
		self.samplerate1 = np.array(self.samplerate)
		wavfile.write(fileName,self.samplerate1, self.out)
	############################# Hamming ############################

	def Hamming(self):
		
		self.data_line3.clear()
		self.data_line4.clear()

		if self.value1 !=0 :
			self.ha=np.hamming(int(len(self.band1)))
			self.h2a=self.band1*self.ha
			
			self.y_FF2a=self.data_FF*self.h2a
			
			self.data_line3.setData(self.h2a)  
			self.data_line4.setData(np.abs(self.y_FF2a)) 
		
		if self.value2 !=0 :
			self.hb=np.hamming(int(len(self.band2)))
			self.h2b=self.band2*self.hb
			
			self.y_FF2b=self.data_FF*self.h2b
			
			self.data_line3.setData(self.h2b)  
			self.data_line4.setData(np.abs(self.y_FF2b)) 
			
		if self.value3 !=0 :
			self.hc=np.hamming(int(len(self.band3)))
			self.h2c=self.band3*self.hc
			
			self.y_FF2c=self.data_FF*self.h2c
			
			self.data_line3.setData(self.h2c)
			self.data_line4.setData(np.abs(self.y_FF2c)) 
		
		if self.value4 !=0 :
			self.hd=np.hamming(int(len(self.band4)))
			self.h2d=self.band4*self.hd
			
			self.y_FF2d=self.data_FF*self.h2d
			
			self.data_line3.setData(self.h2d)  
			self.data_line4.setData(np.abs(self.y_FF2d)) 
		
		if self.value5 !=0 :
			self.he=np.hamming(int(len(self.band5)))
			self.h2e=self.band5*self.he
			
			self.y_FF2e=self.data_FF*self.h2e

			self.data_line3.setData(self.h2e)  
			self.data_line4.setData(np.abs(self.y_FF2e)) 
		
		



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
		self.fs=fs

	def popUpwindow(self):

		global application1
		application1=pop_win()
		application1.show()
		


def main():
	app = QtWidgets.QApplication(sys.argv)
	global application
	application = ApplicationWindow()
	application.show()
	app.exec_()


if __name__ == "__main__":
	main()
