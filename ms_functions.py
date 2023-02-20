def graf_prob_acum(dataframe, columna, medida):
    
    '''
    Esta función permite graficar la función de distribución acumulativa y preguntar 
    por la probabilidad de obtener una medida específica (dado que es acomulativa, 
    técnicamente es la probabilidad de que sea la medida indicada o menor) la cual 
    aparecerá señalada en la curva.
    Args.
        dataframe: El dataframe que tenemos pre-procesado
        columna: El nombre de la columna/variable que deseamos graficar
        medida: La probabilidad específica que queremos consultar
    '''
    import empiricaldist
    
    cdf_variable = empiricaldist.Cdf.from_seq(
    dataframe[columna],
    normalize = True
    )
    
    cdf_variable.plot()

    q = medida
    p = cdf_variable.forward(q)
    
    plt.title(columna, loc = 'left')

    plt.vlines(
        x=q,
        ymin=0,
        ymax=p,
        color='black',
        linestyle='dashed'
    )

    plt.hlines(
        y=p,
        xmin=cdf_variable.qs[0],
        xmax=q,
        color='black',
        linestyle='dashed'
    )

    plt.plot(q,p, 'ro')