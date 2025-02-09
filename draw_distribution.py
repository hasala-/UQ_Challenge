import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 random samples
Xa1_samples = np.random.normal(loc=0.1, scale=0.01, size=1000)

# Plot histogram with KDE (Kernel Density Estimation)
sns.histplot(Xa1_samples, kde=True, bins=30)
plt.axvline(x=0.1, color='r', linestyle='--', label="Mean (μ = 0.1)")
plt.axvline(x=0.1 + 0.02, color='g', linestyle='--', label="μ ± 2σ")
plt.axvline(x=0.1 - 0.02, color='g', linestyle='--')
plt.legend()
plt.xlabel("Xa1 Sample Values")
plt.ylabel("Density")
plt.title("Distribution of Xa1 Samples (Normal: μ=0.1, σ=0.01)")
plt.show()