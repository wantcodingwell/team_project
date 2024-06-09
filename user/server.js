const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static(__dirname));

// Routes
app.post('/submission', (req, res) => {
    const { username, password, code } = req.body;
    console.log(`Received submission from ${username}`);
    console.log(`Password: ${password}`);
    console.log(`Code: ${code}`);
    res.json({ message: 'Submission received!' });
});

// Start server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
