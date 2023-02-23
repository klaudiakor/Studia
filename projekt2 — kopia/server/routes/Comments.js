const express = require("express");
const router = express.Router();

const { Comments } = require("../models");
const { validateToken } = require("../middlewares/AuthMiddleware");

// comments from some post
router.get("/:postId", async (req, res) => {
  const postId = req.params.postId;
  const comments = await Comments.findAll({ where: { GraphicId: postId } });
  res.json(comments);
});

// create comment
router.post("/", validateToken, async (req, res) => {
  // dostaje request -> idzie przez middleware (validateToken) jak jest ok i zostala wywolana funkcja next to -> wykonuje to co jest tu
  const comment = req.body;
  const username = req.user.username;
  comment.username = username;
  const result = await Comments.create(comment);
  console.log(result.id);

  res.json(result);
});

// delete comment
router.delete("/:commentId", validateToken, async (req, res) => {
  const commentId = req.params.commentId

  await Comments.destroy({
    where: {
      id: commentId,
    }
  });
  res.json("deleted successfuly");
});

module.exports = router;