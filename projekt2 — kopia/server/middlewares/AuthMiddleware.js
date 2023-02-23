const { verify } = require("jsonwebtoken");

const validateToken = (req, res, next) => {
    const accessToken = req.header("accessToken");

    // czy uzytkownik próbuje zostawic komentaz bez zalogowania sie
    if (!accessToken) {
        return res.json({ error: "User not logged in!" });
    }

    try {
        const validToken = verify(accessToken, "importantsecret"); // to tak naprawde username i id, kt uzywam do stworzenia tokenu
        req.user = validToken; //user bedzie dostepny w kazdym requescie
        if (validToken) {
            return next(); //można kontynuować request
        }
    } catch (err) {
        return res.json({ error: err });
    }
};

module.exports = { validateToken };