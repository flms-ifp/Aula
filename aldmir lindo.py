eu sou lindo mas luis é mais
a= ("casa")
print (a)



<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Produtos</title>
</head>
<body>
    <header><!--Cabeçalho-->
        <img src="" alt="">
        <h1>GameMarket</h1>
        <form>
            <input type="search" name="pesquisa" id="pesquisa">
            <button type="submit">Logar</button>
            <button type="submit">Cadastrar</button>
            <button type="submit">🛒</button>
        </form>
    </header>
    <main><!--Principal. Muda-->
        <p>Cadastro</p>
        <form>
            
            <label for="nome_produto">Nome do Produto:</label>
            <input type="text" name="nome_produto" id="nome_produto" required>
            
            <br>
            
            <label for="foto_produto">Foto do Produto:</label>
            <input type="file" name="foto_produto" id="foto_produto" required>
            
            <br>
            
            <label for="preco_custo">Preço de Custo:</label>
            <input type="number" name="preco_custo" id="preco_custo" required>
            
            <br>

            <label for="preco_venda">Preço de Venda:</label>
            <input type="number" name="preco_venda" id="preco_venda" required>

            <br>
            
            <label for="descricao_produto">Descrição do Produto:</label>
            <textarea name="descricao_produto" id="descricao_produto"></textarea>

            <br>

            <label for="qtd_estoque">Quantidade de Estoque:</label>
            <input type="number" name="qtd_estoque" id="qtd_estoque" required>

            <br>

            <label for="tamanho_produto">tamanho_produto</label>
            <input type="text" name="tamanho_produto" id="tamanho_produto" required>


        </form>

    </main> 
    <footer><!--Rodapé-->
        <p>✉Email:</p>
        <a href="mailto:awcs@discente.ifpe.edu.br">awcs@discente.ifpe.edu.br</a>
        <p>Instagram:</p>
        <a href="https://www.instagram.com/aldmir">@aldmir</a>
        <br>
        <p>Desenvolvido por Aldmir Willyan</p>
    </footer>
</body>
</html>
