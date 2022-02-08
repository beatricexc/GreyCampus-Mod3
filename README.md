# GreyCampus-Mod3

Linear Regression is used for predictive analysis
- when there is a growth in y, there is a growth in x and viceversa (sales/marketing..when the marketing expenditure increases, the sales increase as well)
- it is always the dependent which changes based on the independent values (logic!)
- we call it linear regression every time there is a change in x with repect to y
- parallel lines are not linear regressions x || o , where o is the fitted line

### Types of Linear Regression
They are mostly defined by 3 parameters: 
1. the number of independent variables
2. shape of the regression line (size) - spread of the data 
3. Type of dependent variables

#### *Polynomyial* : when the data points have a curve at the edge, we use polynomial

![image](https://user-images.githubusercontent.com/72341578/152889483-087ee50c-9f8c-431e-9ec6-0df406ffcc59.png)


 ##### *Logistic Regression* works with binomial distribution and it does not output the relationship between x and y, x != y

 -the values are between 0 to 1 and there is a treshold that comes in between, therefore anything above the treshold is a *yes* and anything below the treshold is a *no*
   
 -we use something called the odds ratio : P / (1-p) 
   
        log(odds) = log(P/(1-p))
        logit(p) = log(P/(1-p))
     
     
- because we're working with binomial distribution, we need to choose a link function *logit*
    
- these parameteres are chosen to maximise the propability(likelyhood) of the sample value 

**Problems** : over fitting and under fitting 
        
        
- Quantile Regression
#### Ridge Regression- used when the data has high levels of multi-collinearity 
! multicolinearity = a situation in which more than two explanatory variables in a multiple regression model are highly linearly correlated
Ridge is a technique/method for analyzing multiple regression data that suffer from multicollinearity. By adding a degree of bias to the regression estimates, ridge regression reduces the standard errors.
- 2 errors occur and they are caused by bis and variance
- to fix the errors, we use a shringage paramater that results in low variance.
- ridge does not take the vlaues to 0 
- regularization method L2

#### Lasso Regresion : least absolute shrinkage and selection operator
- lasso uses absolute values for penalizing as oppossed to ridge 
- it can shrink to 0 also
- L1 regularization 
- the higher the correlation the greater is the shrink to 0


#### Elastic Net Regression : L1+ L2
- hybrid regression
- Gauss Markov Theorem / Assumptions : in linear reg model, then the OLS ( **O**rdinary **L**east **S**quares) will be BLUE (**B**est **L**inear **U**nbiassed **E**stimator)
!NOTE : There are 6 assumptions under Gauss Markov Theorem: 
1. Linearity of parameteres 

                  y = mx + c
                  DB = m(age) + m(salary) + C + Error
                  
          
2. Consistency 
- Principal Component Regression (PCR)
