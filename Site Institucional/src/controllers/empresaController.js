var empresaModel = require("../models/empresaModel");

// function buscarPorCnpj(req, res) {
//   var cnpj = req.query.cnpj;

//   empresaModel.buscarPorCnpj(cnpj).then((resultado) => {
//     res.status(200).json(resultado);
//   });
// }

// function listar(req, res) {
//   empresaModel.listar().then((resultado) => {
//     res.status(200).json(resultado);
//   });
// }

// function buscarPorId(req, res) {
//   var id = req.params.id;

//   empresaModel.buscarPorId(id).then((resultado) => {
//     res.status(200).json(resultado);
//   });
// }

function cadastrar(req, res) {
  var cnpj = req.body.cnpj;
  var razaoSocial = req.body.razaoSocial;
  var cep = req.body.cep;
  var telefone = req.body.telefone;
  var email = req.body.email;
  var senha = req.body.senha

  // empresaModel.buscarPorCnpj(cnpj).then((resultado) => {
  //   if (resultado.length > 0) {
  //     res
  //       .status(401)
  //       .json({ mensagem: `a empresa com o cnpj ${cnpj} já existe` });
  //   } else {
  //     empresaModel.cadastrar(razaoSocial, cnpj,cep,telefone,email,senha).then((resultado) => {
  //       res.status(201).json(resultado);
  //     });
  //   }
  // });
}

module.exports = {
  
  cadastrar
  
};
// buscarPorCnpj,buscarPorId,listar
  
