// Função para criar um novo produto
function cadastrarProduto() {
    const nome = document.getElementById('nome_produto').value;
    const descricao = document.getElementById('descricao').value;
    const valor = parseFloat(document.getElementById('valor').value);
    const quantidade = parseInt(document.getElementById('quantidade').value);
    const categoria = document.getElementById('categoria').value;

    const novoProduto = {
        name: nome,
        description: descricao,
        value: valor,
        quantity: quantidade,
        category: categoria
    };

    fetch('http://localhost:5000/api/insert/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(novoProduto)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Produto cadastrado com sucesso:', data);
        // Aqui você pode atualizar a interface do usuário ou executar ações adicionais após o cadastro
    })
    .catch(error => {
        console.error('Erro ao cadastrar o produto:', error);
    });
}

document.getElementById('cadastrar-btn').addEventListener('click', cadastrarProduto);
