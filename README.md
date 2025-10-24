# Currency Converter

A simple Python application that converts currencies using real-time exchange rates from the ExchangeRate-API.

## Features

- **Real-time Exchange Rates**: Fetches current exchange rates from ExchangeRate-API
- **Caching**: Implements TTL (Time To Live) caching to reduce API calls and improve performance
- **Interactive CLI**: User-friendly command-line interface for currency conversion
- **Error Handling**: Robust error handling for network issues and invalid inputs

## Requirements

- Python 3.6+
- `requests` library
- `cachetools` library

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install requests cachetools
```

## Usage

### Command Line Interface

Run the main script:

```bash
python src/currency_converter.py
```

The program will prompt you to enter:
1. **Base Currency**: The currency you want to convert from (e.g., USD, EUR, GBP)
2. **Target Currency**: The currency you want to convert to (e.g., JPY, CAD, AUD)
3. **Amount**: The amount to convert

### Example

```
Please Enter Base Currency: USD
Please Enter target Currency: EUR
Please Enter Amount: 100
100.0 USD is 85.23 EUR
```

### Jupyter Notebook

You can also run the code interactively using the provided `test.ipynb` notebook for testing and experimentation.

## How It Works

1. **API Integration**: Uses ExchangeRate-API (v6) to fetch real-time exchange rates
2. **Caching**: Implements TTL cache with 300 seconds (5 minutes) expiration to avoid excessive API calls
3. **Currency Conversion**: Calculates the converted amount by multiplying the input amount with the exchange rate

## API Details

- **Provider**: ExchangeRate-API
- **Endpoint**: `https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}`
- **Rate Limiting**: The API has rate limits, which is why caching is implemented
- **Supported Currencies**: Supports 160+ currencies worldwide

## Project Structure

```
Currency Convertor/
├── src/
│   ├── currency_converter.py    # Main application file
│   └── app.py                   # Additional application file
├── test.ipynb                   # Jupyter notebook for testing
└── README.md                    # This file
```

## Error Handling

The application handles various error scenarios:
- Network connectivity issues
- Invalid API responses
- Invalid currency codes
- Invalid numeric inputs

## Configuration

The cache configuration can be modified in the code:
- `maxsize`: Maximum number of cached items (default: 200)
- `ttl`: Time to live in seconds (default: 300 seconds)

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving error handling
- Adding unit tests
- Enhancing the user interface

## License

This project is open source and available under the MIT License.

## Disclaimer

Exchange rates are provided by third-party APIs and may not reflect real-time market conditions. Always verify rates for important financial decisions.
