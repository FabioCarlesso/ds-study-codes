# HDFS PIG

    %DECLARE inputCSV '/user/fabio/input/despesas.csv';
    data = LOAD '$inputCSV' USING PigStorage(';') AS (year:int, name:chararray, spent:float);
    grouped = GROUP data BY name;
    sumSpent = FOREACH grouped GENERATE group, SUM(data.spent);
    STORE sumSpent INTO '/user/fabio/input/resultado' USING PigStorage(';');