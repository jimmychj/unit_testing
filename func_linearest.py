def linearest(param1, param2,param3):
    a = (param1[0]-param2[0]) / (param1[1]-param2[1])
    b = param1[1] - param1[0]*a
    output = a * param3 + b
    return output