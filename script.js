// Função para criar um novo produto
function cadastrarProduto() {
    const nome = document.getElementById('nome_produto').value.trim();
    const descricao = document.getElementById('descricao').value.trim();
    const valor = parseFloat(document.getElementById('valor').value.trim());
    const quantidade = parseInt(document.getElementById('quantidade').value.trim());
    const categoria = document.getElementById('categoria').value.trim();

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

// Função para deletar um produto
function deletarProduto() {
    // Aqui você precisa obter o ID do produto a ser deletado e passá-lo para a API
    const idProduto = 1; // Substitua pelo ID correto do produto a ser deletado
  
    fetch(`http://localhost:5000/api/delete/products/${idProduto}`, {
      method: 'DELETE'
    })
      .then(response => response.json())
      .then(data => {
        console.log('Produto deletado com sucesso:', data);
        // Aqui você pode atualizar a interface do usuário ou executar ações adicionais após a exclusão
      })
      .catch(error => {
        console.error('Erro ao deletar o produto:', error);
      });
  }

// Função para validar o campo Nome
function validarNome() {
    const nomeInput = document.getElementById('nome_produto');
    const nomeValue = nomeInput.value;
    const nomeError = document.getElementById('nome_produto_error');

    // Verifica se o valor contém números ou caracteres especiais
    if (/[\d!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/.test(nomeValue) || nomeValue.trim() === '') {
        nomeError.textContent = 'Nome inválido';
        return false;
    } else {
        nomeError.textContent = ''; // Limpa a mensagem de erro
        return true;
    }
}

// Função para validar o campo Valor
function validarValor() {
    const valorInput = document.getElementById('valor');
    const valorValue = valorInput.value;
    const valorError = document.getElementById('valor_error');

    // Verifica se o valor não é um número ou está vazio ou contém caracteres especiais
    if (isNaN(parseFloat(valorValue)) || !isFinite(valorValue) || valorValue.trim() === '') {
        valorError.textContent = 'Valor inválido';
        return false;
    } else {
        valorError.textContent = ''; // Limpa a mensagem de erro
        return true;
    }
}

// Função para validar o campo Categoria
function validarCategoria() {
    const categoriaInput = document.getElementById('categoria');
    const categoriaValue = categoriaInput.value;
    const categoriaError = document.getElementById('categoria_error');

    // Verifica se o valor contém números ou caracteres especiais
    if (/[\d!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/.test(categoriaValue) || categoriaValue.trim() === '') {
        categoriaError.textContent = 'Categoria inválida';
        return false;
    } else {
        categoriaError.textContent = ''; // Limpa a mensagem de erro
        return true;
    }
}

// Função para validar o campo Quantidade
function validarQuantidade() {
    const quantidadeInput = document.getElementById('quantidade');
    const quantidadeValue = quantidadeInput.value;
    const quantidadeError = document.getElementById('quantidade_error');

    // Verifica se o valor não é um número ou está vazio ou contém caracteres especiais
    if (isNaN(parseInt(quantidadeValue)) || !isFinite(quantidadeValue) || quantidadeValue.trim() === '') {
        quantidadeError.textContent = 'Quantidade inválida';
        return false;
    } else {
        quantidadeError.textContent = ''; // Limpa a mensagem de erro
        return true;
    }
}

// Função para validar o campo Descrição
function validarDescricao() {
    const descricaoInput = document.getElementById('descricao');
    const descricaoValue = descricaoInput.value;
    const descricaoError = document.getElementById('descricao_error');

    // Verifica se a descrição está vazia
    if (descricaoValue.trim() === '') {
        descricaoError.textContent = 'Descrição não pode ser vazia';
        return false;
    } else {
        descricaoError.textContent = ''; // Limpa a mensagem de erro
        return true;
    }
}

// Função para realizar todas as validações
function validarFormulario() {
    const nomeValido = validarNome();
    const valorValido = validarValor();
    const categoriaValida = validarCategoria();
    const quantidadeValida = validarQuantidade();
    const descricaoValida = validarDescricao();

    // Verifica se todos os campos são válidos
    if (nomeValido && valorValido && quantidadeValida && descricaoValida && categoriaValida) {
        return true;
    } else {
        // Se algum campo não é válido, impede o envio do formulário
        return false;
    }
}

// Adiciona um ouvinte de evento para o botão "Cadastrar" que chama a função de validação
document.getElementById('cadastrar-btn').addEventListener('click', function (event) {
    if (!validarFormulario()) {
        event.preventDefault();
    } else {
        // Se o formulário é válido, envia os dados para o servidor
        cadastrarProduto();
    }
    
    // Limpar os campos após o cadastro
    document.getElementById('nome_produto').value = '';
    document.getElementById('descricao').value = '';
    document.getElementById('valor').value = '';
    document.getElementById('quantidade').value = '';
    document.getElementById('categoria').value = '';
});

// Adiciona um ouvinte de evento para o botão "Deletar" que chama a função de deletar
document.getElementById('deletar-btn').addEventListener('click', function (event) {
    if (!validarFormulario()) {
        event.preventDefault();
    } else {
        // Se o formulário é válido, envia os dados para o servidor
        deletarProduto();
    }
    
    // Limpar os campos após o cadastro
    document.getElementById('nome_produto').value = '';
    document.getElementById('descricao').value = '';
    document.getElementById('valor').value = '';
    document.getElementById('quantidade').value = '';
    document.getElementById('categoria').value = '';
});


