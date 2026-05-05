import unittest
from unittest.mock import patch, MagicMock
import converter

class TestCurrencyConverter(unittest.TestCase):
    @patch('converter.tk.Tk')
    @patch('converter.ttk')
    @patch('converter.messagebox')
    @patch('converter.requests')
    def test_validate_input_positive(self, mock_requests, mock_messagebox, mock_ttk, mock_tk):
        app = converter.CurrencyConverterApp(None)
        app.amount_entry = MagicMock()
        app.amount_entry.get.return_value = "123.45"
        self.assertTrue(app.validate_input()[0])

    @patch('converter.tk.Tk')
    @patch('converter.ttk')
    @patch('converter.messagebox')
    @patch('converter.requests')
    def test_validate_input_negative(self, mock_requests, mock_messagebox, mock_ttk, mock_tk):
        app = converter.CurrencyConverterApp(None)
        app.amount_entry = MagicMock()
        app.amount_entry.get.return_value = "-10"
        self.assertFalse(app.validate_input()[0])

    @patch('converter.tk.Tk')
    @patch('converter.ttk')
    @patch('converter.messagebox')
    @patch('converter.requests')
    def test_validate_input_zero(self, mock_requests, mock_messagebox, mock_ttk, mock_tk):
        app = converter.CurrencyConverterApp(None)
        app.amount_entry = MagicMock()
        app.amount_entry.get.return_value = "0"
        self.assertFalse(app.validate_input()[0])

    @patch('converter.tk.Tk')
    @patch('converter.ttk')
    @patch('converter.messagebox')
    @patch('converter.requests')
    def test_validate_input_invalid(self, mock_requests, mock_messagebox, mock_ttk, mock_tk):
        app = converter.CurrencyConverterApp(None)
        app.amount_entry = MagicMock()
        app.amount_entry.get.return_value = "abc"
        self.assertFalse(app.validate_input()[0])
