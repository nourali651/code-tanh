def tanh(x):
    return (2 / (1 + (2.718281828459045 ** (-2 * x)))) - 1  

i1 = 0.05  
i2 = 0.10  

we1, we2 = 0.15, 0.20  
we3, we4 = 0.25, 0.30  

bias_hidden = 0.35  

net_h1 = (we1 * i1) + (we2 * i2) + bias_hidden  
net_h2 = (we3 * i1) + (we4 * i2) + bias_hidden  

out_h1 = tanh(net_h1)  
out_h2 = tanh(net_h2)  

we5, we6 = 0.40, 0.45  
we7, we8 = 0.50, 0.55  

bias_output = 0.60  

net_o1 = (we5 * out_h1) + (we6 * out_h2) + bias_output  
net_o2 = (we7 * out_h1) + (we8 * out_h2) + bias_output  

out_o1 = tanh(net_o1)  
out_o2 = tanh(net_o2)  

print("Final Output of O1:", out_o1)  
print("Final Output of O2:", out_o2)  

target_o1 = 0.1  
target_o2 = 0.99  

error_o1 = 0.5 * ((target_o1 - out_o1) ** 2)  
error_o2 = 0.5 * ((target_o2 - out_o2) ** 2)  

total_error = error_o1 + error_o2  

print("Error at O1:", error_o1)  
print("Error at O2:", error_o2)  
print("Total Network Error:", total_error)  
