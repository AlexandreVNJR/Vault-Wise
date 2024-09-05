var usuarioModel = require("../models/usuarioModel");

 function buscarPorCnpj(req, res) {
   var cnpj = req.query.cnpj;

   usuarioModel.buscarPorCnpj(cnpj).then((resultado) => {
     res.status(200).json(resultado);
   });
 }

//  function listar(req, res) {
//    usuarioModel.listar().then((resultado) => {
//      res.status(200).json(resultado);
//    });
//  }

//  function buscarPorId(req, res) {
//    var id = req.params.id_usuario;

//    usuarioModel.buscarPorId(id).then((resultado) => {
//      res.status(200).json(resultado);
//    });
//   }

// function cadastrar(req, res) {
//   var nome = req.body.nomeServer;
//   var cpf = req.body.cpfServer;
//   var email = req.body.emailServer;
//   var telefone = req.body.telefoneServer;
//   var cargo = req.body.cargoServer;
//   var senha = req.body.senhaServer;
//   var cnpjValidacao

//  usuarioModel.buscarPorCnpj(cnpjValidacao).then((resultado) => {
//    if (resultado.length > 0) {
//      res
//        .status(401)
//        .json({ mensagem: `a usuario com o cnpj ${cnpj} já existe` });
//    } else {
//      usuarioModel.cadastrar(nome, cpf, email, telefone, cargo, senha).then((resultado) => {
//        res.status(201).json(resultado);
//      });
//    }
//  });
// }

function cadastrar(req, res) {
  var nome = req.body.nomeServer;
  var cpf = req.body.cpfServer;
  var email = req.body.emailServer;
  var telefone = req.body.telefoneServer;
  var cargo = req.body.cargoServer;
  var senha = req.body.senhaServer;
  var cnpjValidacao = req.body.cnpjValidacaoServer;

  // Verificar se o CNPJ existe e pegar o cnpj
  usuarioModel.buscarPorCnpj(cnpjValidacao).then(resultado => {
      if (resultado.length > 0) {
          // Recupera o id da empresa a partir do resultado
          var cnpj = resultado[0].cnpj;

          // CNPJ válido, prosseguir com o cadastro do usuário
          usuarioModel.cadastrar(nome, cpf, email, telefone, senha, cargo, cnpj)
              .then(() => {
                  res.status(201).json({ mensagem: "Usuário cadastrado com sucesso!" });
              })
              .catch(erro => {
                  console.error("Erro ao cadastrar o usuário: ", erro);
                  res.status(500).json({ erro: "Erro ao cadastrar o usuário." });
              });
      } else {
          // CNPJ não encontrado
          res.status(404).json({ mensagem: "Empresa com o CNPJ informado não encontrada." });
      }
  }).catch(erro => {
      console.error("Erro ao buscar o CNPJ: ", erro);
      res.status(500).json({ erro: "Erro ao verificar o CNPJ." });
  });
}


module.exports = {
  cadastrar,buscarPorCnpj
};

// buscarPorCnpj,buscarPorId,listar
