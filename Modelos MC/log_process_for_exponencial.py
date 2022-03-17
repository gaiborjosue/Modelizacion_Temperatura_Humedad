# First equation
def func1(x, y, z):
    sum_v = []
    k_sumx = []
    n_l = 0

    for i in range(len(z)):
        sum_v.append(z[i])
        k_sumx.append(x[i])
        n_l += 1

    return print(f"{sum(sum_v)} = k{sum(k_sumx)} + {n_l}L")

func1(temp_datax, hum_datay, hum_datay_log)


def func2(x, y, z):
    x_times_z = []
    for i in range(len(x)):
        x_times_z.append(x[i] * z[i])
    
    k_sumx_squared = []
    for i in range(len(x)):
        k_sumx_squared.append(x[i] ** 2)
    
    l_times_sumx = []
    for i in range(len(x)):
        l_times_sumx.append(x[i])

    return print(f"{sum(x_times_z)} = k{sum(k_sumx_squared)} + {sum(l_times_sumx)}L")

func2(temp_datax, hum_datay, hum_datay_log)