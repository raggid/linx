module.exports = (app) => {
    const controller = app.controllers.recommendations;
    app.route("/recommendations").get(controller.listProducts);
};
