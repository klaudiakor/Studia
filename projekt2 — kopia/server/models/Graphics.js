module.exports = (sequelize, DataTypes) => {

    const Graphics = sequelize.define("Graphics", {
        title: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        description: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        graphics: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        username: {
            type: DataTypes.STRING,
            allowNull: false,
        },

    });

    Graphics.associate = (models) => {
        Graphics.hasMany(models.Comments, {
            onDelete: "cascade",
        });
    };
    return Graphics;
};