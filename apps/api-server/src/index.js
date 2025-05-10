const express = require('express');
const { add } = require('@monorepo-test/utils');

const app = express();
const PORT = 5001;

app.get('/add', (req, res) => {
    const { a, b } = req.query;
    const result = add(a, b);
    res.json({ result: add(Number(a), Number(b)) });
});

app.listen(PORT, () => {

    console.log(`API Server is running on port ${PORT}`);
});