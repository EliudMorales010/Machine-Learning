''' pyplot es un submodulo asi que se puede importar con el aplias plt
- import matplotlib.pyplot as plt
'''

import matplotlib.pyplot as plt
import numpy as np

# Ejemplo:
'''
Dibujar una linea en un diagrama desde la posicion (0,0)
hasta la posicion (6, 250)
'''
xpunto = np.array([0, 6])
ypunto = np.array([0, 250])

plt.plot(xpunto, ypunto)
plt.show()