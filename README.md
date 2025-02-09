<div align="left"> 
<h2>Initial UQ Quantification Model using Bayesian MCMC</h2> 
</div>
This model quantifies uncertainty in two aleatory variables X<sub>a1</sub> and X<sub>a2</sub> as well as the three epistemic variables X<sub>e1</sub>, X<sub>e2</sub>, X<sub>e3</sub> using Bayesian Markov Chain Monte-Carlo (MCMC) sampling.
<p></p>
<h3>Problem:</h3>
Given the back-box local simulation model that takes aleatory variables X<sub>a1</sub>, X<sub>a2</sub>, epistemic variables X<sub>e1</sub>, X<sub>e2</sub>, X<sub>e3</sub>, three control variables X<sub>c1</sub>, X<sub>c2</sub>, X<sub>c3</sub> (control variables are assumed to be constants for this UQ problem) and provides time varying series of outputs (60 time-steps) Y<sub>1</sub>, Y<sub>2</sub>, Y<sub>3</sub>, Y<sub>4</sub>, Y<sub>5</sub>, Y<sub>6</sub>, create an uncertinty model for aleatory and epistemic input variables.
<p></p>
<h3>Theory:</h3>
Using Bayes Theorem:
<p></p>
<img src="https://latex.codecogs.com/svg.latex?P(X|Y)%20=%20\frac{P(X)%20\cdot%20P(Y|X)}{P(Y)}" alt="Bayesian Formula" />
<p></p>  

- P(X) is the prior distribution assumed for each of the aleatory and epistemic variables. For aleatory initial model assumes distribution is normal truncated for the interval [0,1]. Each epistemic variable is assumed to follow a uniform distribution in the interval [0,1]  

- P(Y|X) is the likelihood, which is given by the time-series output of the black-box local model for a set of given inputs.
   
- P(Y) is the normalising constant representing the marginal probability. Since it is difficult to calculate this MCMC is used to approximate the posterior.
  
- P(X|Y) is the posterior distributions for the aleatory and epistemic variables and represents the uncertainty in each input variable. They are found through MCMC sampling.

<h3>Implementing the solution:</h3>
<p></p>  

- Solution is implemented in the following Jupyter Notebook - model1_bayesian_mcmc.ipynb, PyMC is used to create MCMC samples.  

- Local model is executed using the run_model.py script, that takes samples form X variables in input3.txt file. Local model executable provided by the UQ Challenge organisers write output to Y_out.csv file.

<h3>Outputs:</h3>  

- Priors - following histograms shows the prior samples created from the normal (for aleatory) and uniform (for epistemic) distributions. Only 100 samples were used initially since each sample required a local black-box model invocation.  
![Alt Text](./priors.png)

- Posteriors obtained after running the model - following diagrams show posterior distributions obtained after running the MCMC model.
  ![Alt Text](./posterior.png)








