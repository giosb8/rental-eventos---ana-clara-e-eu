document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {

        const cliente = document.querySelector(
            'input[name="cliente_responsavel"]'
        ).value.trim();

        const data = document.querySelector(
            'input[name="data_movimentacao"]'
        ).value;

        const tipo = document.querySelector(
            'select[name="tipo_movimentacao"]'
        ).value;

        const quantidade = document.querySelector(
            'input[name="quantidade"]'
        ).value;

        const equipamento = document.querySelector(
            'select[name="equipamento_id"]'
        ).value;

        if (!cliente || !data || !tipo || !quantidade || !equipamento) {
            event.preventDefault();
            alert("Preencha todos os campos.");
            return;
        }

        if (parseInt(quantidade) <= 0) {
            event.preventDefault();
            alert("A quantidade deve ser maior que zero.");
            return;
        }

        if (tipo !== "Entrada" && tipo !== "Saída") {
            event.preventDefault();
            alert("Selecione um tipo de movimentação válido.");
            return;
        }

    });

});