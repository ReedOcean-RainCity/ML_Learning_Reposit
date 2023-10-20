import numpy as np
import pandas as pd
from sys import exit
from os import getcwd
from os.path import join


class Perceptron:
	def __init__(self):
		self.W = np.array([])
		self.bias = 0
		self.y_pred = []

	def Train(self, X_in, Y_lab):
		try:
			X = pd.DataFrame(data = X_in)
			y = Y_lab.to_numpy()
		except:
			print('failure to parse data')
			return
		else:
			params = np.array(X).shape[1]
			bat_size = y.size
			w = np.zeros((params))
			b = self.bias
			for i in range(0, bat_size):
				yn = y[i]
				for _, x_in in X.iterrows():
					x = x_in.to_numpy()
					temp = w*x
					activ = np.sum(temp)+b
					if (yn*activ)<=0:
						w = np.array(w+(yn*x))
						b = b+yn
			self.W = w
			self.bias = b
		return

	def predict(self, X_in):
		w = self.W
		b = self.bias
		Y = []
		try:
			X = pd.DataFrame(data=X_in)
		except:
			print("failure to read dataset")
			return
		for _, x in X.iterrows():
			x = x.to_numpy()
			temp = np.sum(w*x)+b
			Y.append(temp)
		self.y_pred = np.array(Y)
		return

	def eval(self, y_labs):
		y = y_labs.to_numpy()
		yH = self.y_pred
		n = len(y_labs.index)
		score = 0
		for i in range(0, n):
			score += (y[i]-yH[i])**2
		score /= n
		return score

def numerise(df):
	nums_only = df.select_dtypes(['number'])
	nums_only.dropna(inplace=True)
	return nums_only

def normalise_df(df):
	df_norm = pd.DataFrame(df.copy())
	for col in df_norm.columns:
		df_norm[col] = df_norm[col] / df_norm[col].abs().max()
	return df_norm


def main():
	src = getcwd()
	src = join(src, 'data_unpacked')
	file = join(src, 'Indicadores_Pobresa.xlsx')
	data = pd.read_excel(file, sheet_name = 'data')	# , encoding = 'latin-1'
	adjust = len(data.index)//5
	data = data.sample(n = adjust)

	X = numerise(data)
	X = X.drop(['N_pobreza','ent','mun'], axis = 1)


	Y = pd.DataFrame(data['N_pobreza'])
	Y = numerise(Y)

	x_norm = normalise_df(X)
	y_norm = normalise_df(Y)

	batch = 245
	x_train = x_norm.head(batch)
	x_test = x_norm.tail(batch)
	y_train = y_norm.head(batch)
	y_test = y_norm.tail(batch)

	model = Perceptron()
	model.Train(x_train, y_train)
	model.predict(x_test)
	score = model.eval(y_test)

	print(f'the model was able to predict the number of people in poverty with a mean squared error of {score}')



if __name__ == '__main__':
	main()
