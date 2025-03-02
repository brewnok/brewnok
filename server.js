const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname)));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/about', (req, res) => {
    res.sendFile(path.join(__dirname, 'about.html'));
});

app.get('/contact', (req, res) => {
    res.sendFile(path.join(__dirname,  'contact.html'));
});

app.get('/digital-marketing-services', (req, res) => {
    res.sendFile(path.join(__dirname, 'digital-marketing-services.html'));
});

app.get('/it-services', (req, res) => {
    res.sendFile(path.join(__dirname,  'it-services.html'));
});

app.get('/products', (req, res) => {
    res.sendFile(path.join(__dirname,  'products.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
