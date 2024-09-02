var usuarioModel = require("../models/usuarioModel");

 function buscarPorCpf(req, res) {
   var cpf = req.query.cpf;

   usuarioModel.buscarPorCpf(cpf).then((resultado) => {
     res.status(200).json(resultado);
   });
 }

//  function listar(req, res) {
//    usuarioModel.listar().then((resultado) => {
//      res.status(200).json(resultado);
//    });
//  }

 function buscarPorId(req, res) {
   var id = req.params.id_usuario;

   usuarioModel.buscarPorId(id).then((resultado) => {
     res.status(200).json(resultado);
   });
  }

function cadastrar(req, res) {
  var nome = req.body.nomeServer;
  var cpf = req.body.cpfServer;
  var email = req.body.emailServer;
  var telefone = req.body.telefoneServer;
  var cargo = req.body.cargoServer;
  var senha = req.body.senhaServer;

 usuarioModel.buscarPorCpf(cpf).then((resultado) => {
   if (resultado.length > 0) {
     res
       .status(401)
       .json({ mensagem: `a usuario com o cpf ${cpf} já existe` });
   } else {
     usuarioModel.cadastrar(nome, cpf, email, telefone, cargo, senha).then((resultado) => {
       res.status(201).json(resultado);
     });
   }
 });
}

module.exports = {
  cadastrar,buscarPorCpf
};

// buscarPorCnpj,buscarPorId,listar
