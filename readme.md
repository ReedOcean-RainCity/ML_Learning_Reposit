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
		<h2>Preparing the Data</h2>
		<!--- 			spacer element				--->
		<p>To prepare the data, I needed to sort through what data could be used, and what data I wanted to use. In order to do this,
		I needed to download the dictionary that describes what each piece of data represents. Then, I would mark out what features seemed like
		they might be helpful, and later mark out which ones I would actually use, to make it easier when programming.</p>
		<img src="https://github.com/ReedOcean-RainCity/ML_Learning_Reposit/assets/135147457/4d20e46c-5cea-4a2e-95ac-a79829f6c9b2">
		<!--- 			spacer element				--->
		<img src="https://github.com/ReedOcean-RainCity/ML_Learning_Reposit/assets/135147457/bb2d7855-5a69-421d-bab7-2f199150f856">
		<!--- 			spacer element				--->
		<p>These features were selected because they all relate to the quality of life of the households, as a number, and did not directly
		include the answer within them. To use this data in my, or indeed any, algorithm, I needed to ensure that only numerical values remained
		in each column. Using a combination of functions from the pandas library, designed for this particular kind of problem, removing any text,
		empty variables, or any other kinds of not a number (NaN) elements, the data was ready for use.</p>
		<!--- 			spacer element				--->
		<p>In the case of the script using the scikit learn library, I also needed to convert the dataframes holding the output labels into
		one-dimensional arrays that were compatible with the scikit learn model's functionality of only performing binary classification.</p>
		<!--- 			spacer element				--->
		<h2>Results of the programs:</h2>
		<!--- 			spacer element				--->
		<p>Although my model is far more maleable than the solution provided by scikit learn, it also ssuffers from the lack of optimisation.
		In the time it takes my algorithm to run over a dataset around 3.5 to 4k data entries, the prebuilt model from scikit learn could compute that
		same data 2 or 3 times, and earn a higher accuracy.</p>
		<!--- 			spacer element				--->
		<img src="https://github.com/ReedOcean-RainCity/ML_Learning_Reposit/assets/135147457/d76b25b1-feff-4122-b1d3-84db24b9ac22">
		<!--- 			spacer element				--->
		<p>Changing the ssettings of my model to match the requirements of scikit learn's model, binary classification, causes my algorithm's
		performance to absolutely tank. So while my algorithm is defenitely worse at binary classification than scikit learn's algorithm,
		it is more maleable and can be used to solve more problems.</p>
		<!--- 			spacer element				--->
		<img src="https://github.com/ReedOcean-RainCity/ML_Learning_Reposit/assets/135147457/52f3a574-fc77-47a7-8b0b-dc91a206cf50">
		<!--- 			spacer element				--->
		<h2>Reflecting on the Project</h2>
		<!--- 			spacer element				--->
		<h3>An Unexpected Challenge and Solution</h3>
		<!--- 			spacer element				--->
		<p>Working on this project, I felt that the most difficult part of the work, was to readapt my data and my model in order to perform the
		same task that sscikit learn set their model to do. Though the development of my model itself wassn't hard, and changing my algorithm to
		perform classification wasn't so difficult, what truly was the hardest aspect was figuring out why scikit learn wouldn't accept the
		data that I was attempting to feed it. In the end, I resulted to making use of chatGPT to help me make sense of the error messsages
		that I couldn't quite dechipher on my own. I usually am able to find a solution by looking on the web about what the problem seems to be,
		ocoassianally googling the exact messege I recieved. But, looking through the API reference for sklearn and looking online just wasn't enough
		this time. And, how chatGPT was able to break the error down into plain english made the search for a solution much easier.</p>
		<!--- 			spacer element				--->
		<h3>Applications VS Theory</h3>
		<!--- 			spacer element				--->
		<p>There are many tasks in the world of robotics where machine leanring is useful and can be applied. In this case, an algorithm like mine,
		with a major boost to its compute time, can be helpul when we need a robot to be able to make use of a maleable algorithm that can apply
		for different tasks, but we don't need the algorith to be too complex or precise. </p>
	</body>
</html>
