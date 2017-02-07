## Objetivo

O teste consiste em fazer um crawler para pegar os dados de um arquivo PDF, que pode ser acessado pela página do tesouro.

Precisamos pegar os dados do Boletim FOCUS, publicado semanalmente pelo banco central na página http://www.bcb.gov.br/?FOCUSRELMERC

Na última página de todo Boletim tem algumas informações em uma tabela chamada Expectativas de Mercado.

O que precisamos pegar são os valores dos itens a seguir, para **Médio Prazo**, de 2016, da coluna HOJE.

* IPCA (%)
* IGP-DI (%) 
* IGP-M (%)
* Taxa de câmbio - fim de período (R$/US$)
* Meta Taxa Selic - fim de período (%a.a.)

Ou seja, para o último relatório (http://www.bcb.gov.br/pec/GCI/PORT/readout/R20160324.pdf) os valores seriam de:

* IPCA (%): 7,16
* IGP-DI (%): 7,73
* IGP-M (%): 8,04
* Taxa de câmbio - fim de período (R$/US$): 3,98
* Meta Taxa Selic - fim de período (%a.a.): 13,65

Para tal, nós recomendamos você usar a lib [pdfquery](https://pypi.python.org/pypi/pdfquery/0.2.2#finding-what-you-want), mas sinta-se a vontade para usar outras ferramentas.

**Dica:** Acho que todas as tabelas estão na mesma posição em todos os relatórios, então daria pra vc dar um dump na xml usando `pdf.tree.write(filename, pretty_print=True)` para saber qual o *bbox* de cada item e aí fazer o crawler sempre naquela posição, mas teria que checar a consistência depois.

Finalmente, queria que você gravasse todos esse dados desde o começo de 2015 em um JSON, de forma organizada.

pypdf2

https://github.com/huntrar/scrape

https://github.com/timClicks/slate

**Nota:** O `lxml` deu erro de instalação no Python 3.6.

*Renda Fixa*
