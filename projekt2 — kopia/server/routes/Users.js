const express = require('express');
const router = express.Router();
const bcrypt = require("bcrypt");
const { sign } = require('jsonwebtoken')

const { Users } = require('../models');
const { validateToken } = require('../middlewares/AuthMiddleware')

router.post("/", async (req, res) => {
  const { username, password } = req.body;

  bcrypt.hash(password, 10).then((hash) => {
    Users.create({
      username: username,
      password: hash,
    });
    res.json("success");
  });
});


router.post('/login', async (req, res) => {
  const { username, password } = req.body;

  const user = await Users.findOne({ where: { username: username } });

  if (!user) { res.json({ error: 'User does not exist' }) }
  else {
    bcrypt.compare(password, user.password).then((correctPassword) => {
      if (!correctPassword) { res.json({ error: 'Wrong username and password combination' }) }
      else {
        // user wprowadził prawidłowe dane => tworze token
        const accessToken = sign(
          { username: user.username, id: user.id },
          "importantsecret");
        res.json({ token: accessToken, username: user.username, id: user.id });
      }
    });
  };
});

router.get('/users', validateToken, (req, res) => {
  res.json(req.user);
})

router.get('/basicinfo/:id', async (req, res) => {
  const id = req.params.id;
  const basicInfo = await Users.findByPk(id, { attributes: { exclude: ['password'] } });
  res.json(basicInfo);

});

module.exports = router;