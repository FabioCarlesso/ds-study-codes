# HDFS

    sudo systemctl stop hadoop
    sudo systemctl disable hadoop
    su hadoop

    sejalivre
    /usr/local/hadoop/default/sbin/stop-dfs.sh
    /usr/local/hadoop/default/sbin/start-dfs.sh

    hdfs dfs -mkdir /user/
    hdfs dfs -mkdir /user/fabio
    hdfs dfs -mkdir /user/fabio/input
    hdfs dfs -mkdir /user/fabio/output
    echo "texto simples do exercicio 01" >> texto.txt
    hdfs dfs -put texto.txt /user/fabio/input/
    hdfs dfs -mv /user/fabio/input/texto.txt /user/fabio/output
    hdfs dfs -rm -r /user/fabio/output
