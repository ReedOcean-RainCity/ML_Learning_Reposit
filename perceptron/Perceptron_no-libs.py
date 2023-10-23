import numpy as np
import pandas as pd
from sys import exit
from os import getcwd
from os.path import join
from math import floor, ceil


class Perceptron:
	def __init__(self,*, p_tpye = 'regress', classes=3):
		self.class_num = classes
		self.p_type = p_tpye
		self.W = np.array([])
		self.bias = 0
		self.y_pred = []
		self.score = 0

	def Train(self, X_in, Y_lab):
		try:
			X = pd.DataFrame(data = X_in)
			y = Y_lab.to_numpy()
		except:
			print('failure to parse data')
			return self
		else:
			params = np.array(X).shape[1]
			bat_size = y.size
			w = np.zeros((params))
			b = self.bias
			for i in range(0, bat_size):
				yn = y[i]
				print('\r',f"current cycle {i}/{bat_size}", end="")
				for _, x_in in X.iterrows():
					x = x_in.to_numpy()
					activ = (w*x).sum()+b
					if (yn*activ)<=0:
						w = np.array(w+(yn*x))
						b = b+yn
			print()
			self.W = w
			self.bias = b
		return self

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
		Y = pd.DataFrame(Y)
		if p_type == 'classify':
			Y = self.__encode_onehot(Y,flip=True, num_cats=self.class_num)
		self.y_pred = Y.to_numpy()
		return self

	def __encode_onehot(self,df,*, flip=False, num_cats = 3):
		new_vals=[]
		if num_cats<0:
			print("error: number of categories invalid")
			exit()
		elif num_cats == 1:
			for _,d in df.iterrows():
				v = d.to_numpy()[0]
				if flip:
					vals = 1*v>0.5
				else:
					vals = 1*v<0.5
				new_vals.append(vals)
		elif num_cats == 2:
			for _,d in df.iterrows():
				v = d.to_numpy()[0]
				vals = [1*v<0.5,1*v>0.5]
				if flip:
					vals.reverse()
				val_arr = np.array(vals)
				new_vals.append(val_arr.reshape(val_arr.size,))
		else:
			Max = df.max(axis=0).to_numpy()[0]
			Min = df.min(axis=0).to_numpy()[0]
			R = Max-Min
			frac = [ ((i/num_cats)*(R)) for i in range(1,num_cats+1)]
			frac[num_cats-1] = ceil(frac[num_cats-1])
			for _,d in df.iterrows():
				v = d.to_numpy()[0]
				vals = [1*(v<frac[0])]
				vals += [1*(v>frac[i] and v<frac[i+1]) for i in range(num_cats-1)]
				if  flip:
					vals.reverse()
				val_arr = np.array(vals)
				new_vals.append(val_arr.reshape(val_arr.size,))

		onehot_df = pd.DataFrame({'poverty_rates': new_vals})
		return onehot_df

	def eval(self, y_labs,*, metric='mse'):
		match metric:
			case 'mse':
				self.score = self.__mse(y_labs)
			case 'accuracy':
				self.score = self.__accuracy(y_labs)
		return self

	def __accuracy(self, y_labs):
		Y = self.__encode_onehot(y_labs, num_cats=self.class_num)
		yH = self.y_pred
		Sum = 0
		n = len(Y.index)
		for i, item in Y.iterrows():
			y = item.to_numpy()
			#print(f"y:{y}\nyH:{yH[i]}")
			Sum += 1*(y==yH[i])
			#print(Sum)
		#exit()
		return (Sum).sum()/n


	def __mse(self, y_labs):
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
	data = pd.read_excel(file, sheet_name = 'data')
	n = len(data.index)
	data = data.sample(n=n)


	features = ['perrankin_pe','perrankin_p','N_plb_m','N_plb','N_ic_ali','N_ic_sbv','N_ic_cv','N_ic_segsoc']
	features+=  ['N_ic_asalud','N_ic_rezedu','N_npnv','N_vul_ing','N_vul_car','pobtot_ajustada']
	features.reverse()
	X = data[features]
	X = numerise(X)

	Y = pd.DataFrame(data['N_pobreza'])
	Y = numerise(Y)

	x_norm = normalise_df(X)
	y_norm = normalise_df(Y)

	tr_div = 0.8
	te_div = 0.2
	tr_bat = floor(n*tr_div)
	te_bat = floor(n*te_div)
	x_train = x_norm.head(tr_bat)
	x_test = x_norm.tail(te_bat)
	y_train = y_norm.head(tr_bat)
	y_test = y_norm.tail(te_bat)

	model = Perceptron(p_type = 'classify', classes=1)
	print("beginning training...")
	model.Train(x_train, y_train)
	print("making predictions...")
	model.predict(x_test)
	print("evaluating score...")
	score = model.eval(y_test, metric='accuracy').score
	print(f'the model was able to predict the severity of poverty with an accuacy of {score}')



if __name__ == '__main__':
	main()
