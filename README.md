# LinearRegression
<p>Simple Linear Regression algorithm created in python from scratch (no Machine Learning Libraries used).</p>
<p>
<h1>Installation</h1>
Just download the script from git.<br>
Then install the additional libraries:<br>
<b>(sudo) pip install matplotlib<br>
(sudo) pip install numpy<br>
(sudo) pip install drawnow<br></b>
</p>
<p>
<h1>How to use it?</h1>
Run the script from console:<br>
python LinearRegression.py argv1 argv2 argv3 argv4<br>
argv1 - is the training data. It should be formated like train.csv. The first column represents the x value, the second represents the y value<br>
argv2 - is the output file. The script will output 2 values(t0 and t1) representing the coefficients of the hypothesis:<br>
h(x)=t0+x*t1<br>
argv3 - is the learning rate alfa<br>
argv4 - is a threshold value.<br>
Gradient Descent stops when abs(oldCostFunctionValue-CostFunctionValue)'<'threshold. For better accuracy use a lower threshold value (ex:0.01)<br>
Command example:<br>
<b>python LinearRegression.py train.csv model.txt 0.0001 1</b><br>
</p>
<p>
<h1>Details</h1>
For more information on the topic check out <a href='https://www.coursera.org/learn/machine-learning'>Andrew Ng's Machine Learning Course</a>.<br>
<h2>Hope you enjoy it!</h2>
</p>

