import random, time, hashlib, os, shutil

class moverFile():
	def __init__(self, extSaves=None, inFiles=None, dirNameSaves=None, funcProgress=None):
		self.extSaves = extSaves
		self.funcProgress = funcProgress
		self.inFiles = inFiles
		self.dirNameSaves = dirNameSaves
		self.allPathSaves = self.inFiles
		if (extSaves == None):
			self.extSaves = ["png", "jpg", "jpeg", "bmp"]
		if (inFiles == None):
			self.inFiles = os.getcwd()
		if (dirNameSaves == None):
			self.dirNameSaves = "SaveExt" 
		self.startMoveFile()

	def startMoveFile(self):
		self.allFiles = []
		self.allDirs = []
		self.allExtFiles = []
		self.getAllFilesDirs(self.inFiles)
		self.getRepeatExtFiles(self.allFiles)
		self.mkdirAllExtFiles(self.allExtFiles)
		self.mvAllExtFiles(self.allFiles)

	def getAllFilesDirs(self, path):
		for i in os.listdir(path):
			if (not (self.dirNameSaves in path+i)):
				if (os.path.isdir(path+"/"+i)):
						self.getAllFilesDirs(path+"/"+i)
						self.allDirs.append(path+"/"+i)
				if (os.path.isfile(path+"/"+i)):
					if (self.getExtFile(i) in self.extSaves):
						self.allFiles.append(path+"/"+i)
		return self.allFiles, self.allDirs

	#get Extension Filename
	def getExtFile(self, path):
		for i in range(len(os.path.splitext(path))-1, 0, -1):
			if (os.path.splitext(path) == ""\
				or os.path.splitext(path) == " "\
				or os.path.splitext(path) == None):
				continue
			if (os.path.splitext(path)[0] == "."):
				return os.path.splitext(path)[i][1:]
			else:
				return os.path.splitext(path)[i][1:]
	
	def getRepeatExtFiles(self, allFiles):
		for i in allFiles:
			if (not (self.getExtFile(i) in self.allExtFiles)):
				self.allExtFiles.append(self.getExtFile(i))
		return self.allExtFiles
	
	def mkdirAllExtFiles(self, allExtFiles):
		# если нет каталога сохранения
		if (not os.path.isdir(self.allPathSaves+"/"+self.dirNameSaves)):
			#создаем каталог в котором храним все полученное
			os.mkdir(self.allPathSaves+"/"+self.dirNameSaves)

		#если не существует каталога для файлов без расширений
		if (not os.path.isdir(self.allPathSaves+"/"+self.dirNameSaves+"/noExt")):
			# создаем каталог для файлов без расширений
			os.mkdir(self.allPathSaves+"/"+self.dirNameSaves+"/noExt")
		# перебираем все полученные расширения
		for i in allExtFiles:
			# если это строка
			if (isinstance(i, str)):
				# если она не пустая
				if (i != " " and i != ""):
					#если каталог под названием расширения файла не существует
					if (not os.path.isdir(self.allPathSaves+"/"+self.dirNameSaves+"/"+i)):
						#создаем катлог с расширением файла
						os.mkdir(self.allPathSaves+"/"+self.dirNameSaves+"/"+i)
	def mvAllExtFiles(self, allFiles):
		b = 0
		maxb = len(allFiles)
		for i in allFiles:
			b += 1
			if (os.path.isfile(i)):
				if (self.getExtFile(i) != ""):
					if (self.getExtFile(i)[0] == "."):
						shutil.move(i, self.allPathSaves+"/"+self.dirNameSaves+"/"+self.getExtFile(i)[1:]+"/"+os.path.basename(i))
					else:
						shutil.move(i, self.allPathSaves+"/"+self.dirNameSaves+"/"+self.getExtFile(i)+"/"+os.path.basename(i))
				else:
					shutil.move(i, self.allPathSaves+"/"+self.dirNameSaves+"/"+"noExt/"+self.getExtFile(i)+os.path.basename(i))
			if (self.funcProgress != None):
				self.funcProgress(b, maxb)
