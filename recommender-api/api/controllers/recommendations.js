const { response } = require('express');

module.exports = app => {
    const controller = {};
    const axios = require('axios');
    const rootUrl = 'https://wishlist.neemu.com/onsite/impulse-core/ranking/'
    const productUrl = 'http://catalog:8000/products/'

    controller.listProducts = (req, res) => {
        let maxProducts = req.query.maxProducts > 10 ? req.query.maxProducts : 10;
        let recommended = new Set();
        let resBody = {"mostpopular": [], "pricereduction": []};

        axios.all([
            axios.get(rootUrl + 'mostpopular.json'),
            axios.get(rootUrl + 'pricereduction.json')
        ]).then(
            axios.spread((resp1, resp2) => {
                for(i = 0; i < (maxProducts * 2); i++){
                    recommended.add(resp1.data[i].recommendedProduct['id']);
                    recommended.add(resp2.data[i].recommendedProduct['id']);
                };

                axios.post(productUrl, [...recommended]).then(response => {
                    for(i = 0; i < (maxProducts * 2); i++){
                        if (resBody['mostpopular'].length < maxProducts){
                            let currentId = resp1.data[i].recommendedProduct['id'];
                            let product = response.data[currentId];
                            if (product && product['status'] == 'AVAILABLE'){
                                resBody['mostpopular'].push(product);
                            }
                        }

                        if (resBody['pricereduction'].length < maxProducts){
                            let currentId = resp2.data[i].recommendedProduct['id'];
                            let product = response.data[currentId];
                            if (product && product['status'] == 'AVAILABLE'){
                                resBody['pricereduction'].push(product);
                            }
                        }
                    }

                    res.status(200).json(resBody);
                }).catch(error => {
                    console.log(error);
                })

            })
        ).catch(error => {
            console.log(error);
        });

    };

    return controller;
};
