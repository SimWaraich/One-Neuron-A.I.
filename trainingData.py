from numpy import exp, array, random, dot

training_set_inputs = array([ [0, 0, 1], 
                              [1, 1, 1], 
                              [1, 0, 1], 
                              [0, 1, 1]])
                              
training_set_outputs = array([[0, 1, 1, 0]]).T

random.seed(1)

synaptic_weights = 2 * random.random((3, 1)) - 1

#Outputs current weighting on nodes
print(synaptic_weights)

#AI is trained for 10k generations
for iteration in range(10000):

  #sigmoid function below
    
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    
    #Graphical fluff to output
    print(output)
    
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    
print (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))
