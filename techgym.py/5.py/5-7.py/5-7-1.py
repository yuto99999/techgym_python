import numpy as np

friends = np.array(['太郎','花子','二郎','三郎','良子'])
for i, friend in enumerate(friends):
    print(f"{i + 1}人目 {friend}")