import numpy as np
from scipy.special import cbrt

def handler(event, context):
    print("I like test", np.pi)

    cb = cbrt([27, 64])
    print(cb)

    return {"message": "Successfully executed"}
