# :shopping_cart: Racha Conta :shopping_cart:  

## Um programa em Python para rachar a conta do supermecado  

***Como funciona?***  

Crie um arquivo com a lista de compras, o arquivo deve ter o nome do item, a quantidade a ser comprada e o preço em centavos separados por vígulas, cada item novo deve ser adicionado em uma nova linnha seguindo o mesmo padrão, o arquivo deve ficar assim:  

Feijão,10,750  
Arroz,5,1750  
Iorgute,3,550  

Crie um arquivo com a lista de emails das pessoas que irão rachar conta, o arquivo deve segui esse padrão:  

email1@vaipagaraconta.com  
email2@vaipagaraconta.com  
email3@vaipagaraconta.com  

Depois que os arquivos estiverem criados, execute o seguinte comando:  
*python racha_conta.py arquivo_lista_compras arquivo_emails*  

Para que o comando acima funcione é necessário ter o Python na versão 3 ou superior instalado, o arquivo racha_conta.py deve está na mesma pasta que os arquivos com a lista de compras e o arquivo com a lista de emails, caso não esteja é necessário especificar o caminho dos arquivos e não esqueça de substituir o *arquivo_lista_compras* e *arquivo_emails* pelos nomes dos arquivos que você criou.  

O comando retornará um dicionário com o email e o valor em centavos que cada um deverá pagar, com os dados do exemplo acima o retorno seria:  

*\{'email3@vaipagaraconta.com': 5967, 'email1@vaipagaraconta.com': 5967, 'email2@vaipagaraconta.com': 5966\}*  

Esse programa pode ser usado para dividir outras contas também como a conta da cerveja :beers: .  

Além disso o programa pode ser importado como um módulo do Python e você pode utiliza a função rachar_conta() passando os arquivos com a lista de compras e a lista de emails que vão rachar a conta.  
