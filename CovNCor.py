import scipy
import numpy as np

stockX = np.array([.03,.05,-.03,.02,-.07,.15,.02])
stockY = np.array([.05,.08,-.01,-.01,-.08,.06,.01])


# Covariance - reflects relationship between 2 variables
    # Similar to variance in that is involves the difference of a value from the mean
    # BUT - where variance involves the square of the difference of each value from the mean
    # ...covariance involves for each value of 2 variables, the product of the difference
    # of one varible betweemn the difference of another variable

# Covariance increases as the differnece from the mean when x and y move together for a given 
# varaible with respect to their respeoctive mean
print (stockX)
print (stockY)

#Correlation - speak quantitatively about the relationship between 2 variables
    #Normalized verison of covariance rnaging form -1 to +1
    #Covaraibnce / product of standard deviations of the variables
print(np.mean(stockX))
print(np.std(stockX,))
print(np.std(stockX, ddof=1))



covXY = np.cov(stockX, stockY)
print ("Covariance of X and Y is {}".format(covXY))

corrXY = np.corrcoef(stockX, stockY)[0][1]
print ("Correlation of X and Y is {}".format(corrXY))

###################################################################

#Linear combinations
    #Portfolio of stocks where weights on the variables sum to 1 (40% in X, 60% in Y)
# Probably best done in Excel??

#linear combination is applying a weighted average to two datasets


