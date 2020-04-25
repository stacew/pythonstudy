import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
x=['lee','lee2','lee3','lee4']
y =[100, 200, 105, 300]
plt.plot(x, y, label='label_score', linestyle='dashed', lw=5, color='red', marker='o')
plt.title('score 한글 test')
plt.legend()
plt.ylabel('score')
plt.show()