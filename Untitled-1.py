# %%
import pickle
with open('saved_dictionary.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)

print(loaded_dict)
        

# %%
print(loaded_dict)
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.array([a[0] for a in loaded_dict.keys()])
Y = np.array( [a[1] for a in loaded_dict.keys()])
print(X.shape)
print(Y.shape)

Z =np.array([a for a in loaded_dict.values()])

ax.scatter3D(X, Y, Z, c=Z, cmap='Greens');
ax.set_xlabel('L1 alpha')
ax.set_ylabel('L2 alpha')
ax.set_zlabel('Accuracy')
plt.show()
# Plot the surface.


# %%
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.

ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)




# %%
show()
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.

ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)





