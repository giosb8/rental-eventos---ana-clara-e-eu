function login() {

    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;
    let msg = document.getElementById("mensagem");

    if (email == "" || senha == "") {

        msg.innerHTML = "Preencha e-mail e senha.";

        setTimeout(() => {
            msg.innerHTML = "";
        }, 2000);

        return;
    }

    fetch("/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email: email,
            senha: senha
        })

    })

    .then(response => response.json())

    .then(data => {

        if (data.status === "sucesso") {

            window.location.href = "/principal";

        } else {

            msg.innerHTML = data.mensagem;

            setTimeout(() => {

                msg.innerHTML = "";

                document.getElementById("senha").value = "";

            }, 2000);
        }

    })

    .catch(error => {

        console.error(error);

        msg.innerHTML = "Erro ao conectar com o servidor.";

    });
}