from xlsxreader import ExcelDataReader
import matplotlib.pyplot as plt


from scipy import stats
import numpy as np
import statistics



# Exercise A)

print(30 * "*" + " Exercício A " + 30 * "*")

mu, sigma = 3, 0.5
normal_dist = np.random.normal(mu, sigma, 1000)


n = stats.norm(loc=mu, scale=sigma)

prob_2_years = n.cdf(2)

prob_2_4_years = n.cdf(4) - n.cdf(2)


print("A porcentagem de baterias que duram 2 anos é : {}".format(prob_2_years))
print("A porcentagem de baterias que duram entre 2 e 4 anos é : {}".format(prob_2_4_years))

# count, bins, ignored = plt.hist(normal_dist, 100, normed=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
# plt.show()

print(30 * "*" + " Fim " + 30 * "*")

# Exercise B)
print(30 * "*" + " Exercício B " + 30 * "*")

mu, sigma = 75, 5.5
normal_dist = np.random.normal(mu, sigma, 1000)


n = stats.norm(loc=mu, scale=sigma)

prob_menor_que_60 = n.cdf(60)

prob_maior_que_90 = 1 - n.cdf(90)


print("A probabilidade de ser menor que 60 é : {}".format(prob_menor_que_60))
print("A probabilidade de ser maior que 90 é : {}".format(prob_maior_que_90))


print(30 * "*" + " Fim " + 30 * "*")


# Exercise C)
print(30 * "*" + " Exercício C " + 30 * "*")
mu, sigma = 23, 5

n = stats.norm(loc=mu, scale=sigma)

prob_maior_que_21 = n.cdf(21)
prob_menor_que_27 = n.cdf(27)

prob_t_21_27 = prob_menor_que_27 - prob_maior_que_21

print("O numero de dias de janeiro com chuva"
      " entre 21 e 27 é de {} dias".format(prob_t_21_27 * 31))

print(30 * "*" + " Fim " + 30 * "*")

# Exercise D)

print(30 * "*" + " Exercício " + 30 * "*")

d_data_pure = ExcelDataReader('data/exe_11.xlsx', usecols=(0, 1), l1=2)
d_data_list = [i for i in list(zip(*(d_data_pure.dados())))[1]]
d_data = np.array(d_data_pure.dados()).transpose()
mu = statistics.mean(d_data[1])
var = statistics.variance(d_data[1])
sigma = statistics.stdev(d_data[1])

print("Media: {},\nvariancia: {},\ndesvio padrão: {}".format(mu, var, sigma))

print("Teste de Kosmogorov-Smirnov: ")
dados_padronizados = [(i-mu)/sigma for i in d_data_list]
kstest_result = stats.kstest(rvs=dados_padronizados, cdf='norm')

print(kstest_result)

x_teorica = np.linspace(stats.norm.ppf(0.001), stats.norm.ppf(0.999), 30)
plt.plot(x_teorica, stats.norm.pdf(x_teorica), 'r-', lw=5, alpha=0.6, label='norm pdf')

plt.hist(dados_padronizados, 20, normed=True)
plt.show()

sorted_dados_pad = sorted(dados_padronizados)

print(dados_padronizados)

sorted_dados_pad = [(i - min(sorted_dados_pad))/(max(sorted_dados_pad) - min(sorted_dados_pad)) for i in sorted_dados_pad]
plt.plot((sorted_dados_pad))
plt.plot(sorted(stats.norm.pdf(x_teorica)))
plt.show()

print(30 * "*" + " Fim " + 30 * "*")
# Exercise E)
#
# print(30 * "*" + " Exercício " + 30 * "*")
# print(30 * "*" + " Fim " + 30 * "*")