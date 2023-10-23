<!DOCTYPE html>
<html>
	<head>
		<h1>Development of Perceptron Algorithms for Binary Classification</h1>
	</head>
	<body>
		<h2>Design Choices</h2>
		<p>Coming into this project, I first set out to implement a perceptron algorithm, in accordance to the algorithm found <a href="http://ciml.info/dl/v0_99/ciml-v0_99-ch04.pdf">here.</a></p>
		<!--- 			spacer element				--->
		<img src = "https://github.com/ReedOcean-RainCity/ML_Learning_Reposit/assets/135147457/f0d92e38-0bef-472c-aa30-eae050cee6ca"> 
		<!--- 			spacer element				--->
		<p>My approach in completing this task was very head on. The first thing that I did was start by building the class and the initialisation function.
			I then defined some variables that might be useful, knowing they were subject to change.
			Then, I started first on the trainging, and then the prediction functions. it initially started looking almost exactly the same as the algorithm in figure 1 depicts and,
		except for all the specifics of adjusting the data in python, the code is exceptionally faithful to the source material.</p>
		<!--- 			spacer element				--->
		<p>This approach comes mostly from the fact that, although I understand the intuition _behind_ the algorithm, I still need to know the maths
		behind it in order to program it. And, given that I hadn't much time to implement the algorithms, the approach of understanding the math start to finish,
		in order to create a more efficient and effective approach, I instead had to rely on the work of someone else.</p>
		<!--- 			spacer element				--->
		<p>Initially, I had coded my perceptron to solve regression tasks, however, reviewing the objectives of the project, I realissed I would have to repurpose
		the perceptron class provided by the scsikit learn library to do the same. And some research into the subject revealed, it would be much easier to 
		repurpose my model to perform classification insstead. To do so, I needed to create a one-hot encoder, to convert my continous variable, into a
		binary category set that the scikit learn model could handle.</p>
		<!--- 			spacer element				--->
		<h2>Results of the programs:</h2>
		<p>Although my model is far more maleable than the solution provided by scikit learn, it also ssuffers from the lack of optimisation.
		In the time it takes my algorithm to run over a dataset around 3.5 to 4k data entries, the prebuilt model from scikit learn could compute that
		same data 2 or 3 times, and earn a higher accuracy.</p>
		<img src="https://github.com/ReedOcean-RainCity/ML_Learning_Reposit/assets/135147457/d76b25b1-feff-4122-b1d3-84db24b9ac22"></img>
	</body>
</html>
