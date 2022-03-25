# Spark Despesas

    val dfData = spark.read.option("header", "true").option("inferschema", "true").option("sep", ",").csv("hdfs://localhost:8020/user/fabio/input/despesas.csv")
    val dfDataFilter = dfData.filter("orgao != 'GOVERNO MUNICIPAL'")
    val dfGroupAnoOrgao = dfDataFilter.groupBy("ANO", "ORGAO").sum("DESPESA")
    val dfFilterGroupOrder = dfGroupAnoOrgao.orderBy("ORGAO")
    dfFilterGroupOrder.write.option("header","true").option("sep",";").csv("hdfs://localhost:8020/user/fabio/input/result")