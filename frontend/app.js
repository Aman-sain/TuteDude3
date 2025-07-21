const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const axios = require('axios');

const app = express();
const PORT = 3001;

// Use BACKEND_URL from environment variable or fallback
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';

// Set view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Static files
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('index', { error: null, success: null });
});

app.post('/submit', async (req, res) => {
  const { name, email } = req.body;
  try {
    const response = await axios.post(`${BACKEND_URL}/submit`, { name, email });
    res.render('index', { success: response.data.message, error: null });
  } catch (err) {
    const errorMsg = err.response?.data?.message || 'Something went wrong';
    res.render('index', { success: null, error: errorMsg });
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend listening on http://localhost:${PORT}`);
});
