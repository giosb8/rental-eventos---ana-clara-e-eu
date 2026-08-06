// Usuário de exemplo
const usuarioCorreto = "admin";
const senhaCorreta = "1234";

function login(){

    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("senha").value;
    let msg = document.getElementById("mensagem");

    if(usuario == "" && senha == ""){
        msg.innerHTML = "Preencha usuário e senha.";

        setTimeout(() => {
            msg.innerHTML = "";
        }, 2000);

        return;
    }

    if(usuario != usuarioCorreto){
        msg.innerHTML = "Usuário não encontrado.";

        setTimeout(() => {
            msg.innerHTML = "";
            document.getElementById("usuario").value = "";
            document.getElementById("senha").value = "";
        }, 2000);

        return;
    }

    if(senha != senhaCorreta){
        msg.innerHTML = "Senha incorreta.";

        setTimeout(() => {
            msg.innerHTML = "";
            document.getElementById("senha").value = "";
        }, 2000);

        return;
    }

    // Login correto
    document.getElementById("login").style.display = "none";
    document.getElementById("principal").style.display = "block";

    document.getElementById("nomeUsuario").innerHTML = usuario;
}

function logout(){

    document.getElementById("principal").style.display = "none";
    document.getElementById("login").style.display = "block";

    document.getElementById("usuario").value = "";
    document.getElementById("senha").value = "";
    document.getElementById("mensagem").innerHTML = "";
}

function cadastro(){
    alert("Abrirá a interface de Cadastro de Equipamentos.");
}

function gestao(){
    alert("Abrirá a interface de Gestão de Equipamentos.");
}