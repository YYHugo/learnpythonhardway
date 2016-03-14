import pandas

delimiter_char = ';';

colnames = 'Canal', 'OSA', 'Porta 1', 'Erro', 'Porta 2', 'Erro', 'Porta 3', 'Erro', 'Porta 4', 'Erro'
data = pandas.read_csv(sys.argv[1], names=colnames)