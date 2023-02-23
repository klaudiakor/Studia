const express = require('express');
const router = express.Router();

const { Graphics } = require('../models');
const { validateToken } = require("../middlewares/AuthMiddleware");


//get a list of all the different graphics
router.get("/", async (req, res) => {
    const listOfGraphics = await Graphics.findAll();
    res.json(listOfGraphics);
});

router.get('/byId/:id', async (req, res) => {
    const id = req.params.id;
    const post = await Graphics.findByPk(id);
    res.json(post);
});

router.get('/byUserId/:id', async (req, res) => {
    const id = req.params.id;
    const listOfGraphics = await Graphics.findAll({
        where: {
            UserId: id
        }
    });
    res.json(listOfGraphics);
});

//creates and add new graphics
router.post("/", validateToken, async (req, res) => {
    const post = req.body;
    post.username = req.user.username;
    post.UserId = req.user.id;
    await Graphics.create(post);
    res.json(post);
});

module.exports = router;