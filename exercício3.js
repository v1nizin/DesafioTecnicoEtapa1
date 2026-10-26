function contarPorSituacao(pedidos) {
  let resumo = {};

  for (let i = 0; i < pedidos.length; i++) {
    let s = pedidos[i].situacao;

    if (resumo[s] == undefined) {
      resumo[s] = 0;
    }

    resumo[s] = resumo[s] + 1;
  }

  return resumo;
}

console.log(contarPorSituacao([
  { id: 1, situacao: "Faturado" },
  { id: 2, situacao: "Aberto" },
  { id: 3, situacao: "Faturado" }
]));