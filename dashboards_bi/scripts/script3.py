import matplotlib.pyplot as pyplot


plt.plot(dataset.Sales,dataset.Profit,'go')
plt.title('Relacionamento entre Vendas e Lucro')
plt.xlabel('Vendas')
plt.ylabel('Lucro')
plt.grid(True)
plt.tight_layout()
plt.show()