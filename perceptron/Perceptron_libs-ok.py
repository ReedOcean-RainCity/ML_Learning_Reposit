import numpy as np
import pandas as pd
from sys import exit
from os import getcwd
from math import floor, ceil
from os.path import join as j
from sklearn.linear_model import Perceptron


def numerise(df):
	nums_only = df.select_dtypes(['number'])
	nums_only.dropna(inplace=True)
	return nums_only

def normalise(df):
	df_norm = pd.DataFrame(df.copy())
	for col in df_norm.columns:
		df_norm[col] = df_norm[col] / df_norm[col].abs().max()
	return df_norm

def encode_onehot(df,*, flip=False, num_cats = 3):
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

def main():
	f = j(getcwd(), 'data_unpacked/Indicadores_Pobresa.xlsx')
	data = pd.read_excel(f, sheet_name='data')
	n = len(data.index)
	data = data.sample(n=n)

	features = ['perrankin_pe','perrankin_p','N_plb_m','N_plb','N_ic_ali','N_ic_sbv','N_ic_cv','N_ic_segsoc']
	features+=  ['N_ic_asalud','N_ic_rezedu','N_npnv','N_vul_ing','N_vul_car','pobtot_ajustada']
	features.reverse()
	X = data[features]
	X = numerise(X)

	Y = pd.DataFrame(data['N_pobreza'])
	Y = numerise(Y)

	x_norm = normalise(X)
	y_norm = normalise(Y)
	cats = 1
	y = encode_onehot(y_norm, num_cats=cats)

	if len(X.index)!= n:
		n = len(X.index)
	tr_div = 0.8
	te_div = 0.2
	tr_bat = floor(n * tr_div) 
	te_bat = floor(n * te_div)

	x_train = x_norm.head(tr_bat)
	x_test = x_norm.tail(te_bat)
	y_train = y.head(tr_bat).values.ravel()
	y_test = y.tail(te_bat).values.ravel()

	model = Perceptron()
	print("training model...")
	model.fit(x_train, y_train)
	print("scoring model")
	score = model.score(x_test,y_test)
	print(f"the model was able to predict with an accuracy of: {score}")


if __name__ =="__main__":
	main()
