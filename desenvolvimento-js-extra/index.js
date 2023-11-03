// Crie um projeto com dois arquivos: index.html e script.js. No arquivo 'index' insira apenas a estrutura base HTML e a tag script para conectar o arquivo HTML com o arquivo de extensão JavaScript.

// Usando os conceitos aprendidos nesse módulo, e sem alterar o arquivo index.html, adicione um título simples ao site com o id 'titulo', e um elemento que represente um produto à venda. O produto precisa incluir pelo menos o nome, a descrição e o preço. Pode incluir outros "elementos filhos" se achar necessário como, por exemplo, uma imagem. Procure usar o método simples e o método complexo, ensinados neste tópico.

let elementBody = document.getElementsByTagName('body')[0];

let elementH1 = document.createElement('h1');
elementH1.id = "titulo";
elementH1.innerText = "Título da Página";

let productArticle = document.createElement('div');
productArticle.id = "produto";
productArticle.innerHTML = `<h2>Produto à venda</h2>
<p>Artigo de Colecionador</p>
<p>R$500</p>`
productArticle.style.backgroundColor = 'black';
productArticle.style.color = 'white';
productArticle.style.width = '33%';
productArticle.style.textAlign = 'center';

elementBody.innerHTML = elementH1.outerHTML

elementBody.appendChild(productArticle);
