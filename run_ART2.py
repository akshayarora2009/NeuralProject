from ART2 import ART2
import numpy as np

input_data = np.array([0.8, 0.6])
nn = ART2(n=len(input_data), m=2, rho=0.9, theta=0.1)

nn.start_logging(to_console=True, to_file=False)
nn.learning_trial(idata=input_data)
nn.stop_logging()
