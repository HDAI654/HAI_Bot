# HAI_Bot

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

HAI_Bot is a Python library that allows you to create a custom AI assistant to help with various tasks. You can train the AI with your own data to improve its performance.

## Features
- Trainable with custom data
- Natural Language Processing (NLP) for better interactions
- Customizable model based on user needs

## Installation

To install this library, use pip:

```bash
pip install HAI_Bot
```

or you can install library from existing .gz file.
```bash
pip install hai_bot-0.5.tar.gz
```

## Usage

### Basic Example
```python
from HAI_Bot import HAI_model
n = HAI_model("NLP_Data.json", "chatbot_model.h5")

while True:
  m = str(input("TEXT ==>  ")).lower()
  if m == 'quit':
    break
  print(n.Chat(m))
```

### Using Test Data
The `Test` folder contains sample training data and test scripts:
- `chatbot_model.h5`: A pre-trained model for quick testing.
- `NLP_Data.json`: A structured dataset used for training.
- `Test.py`: A script demonstrating how to use the chatbot.

To test the chatbot using existing data:
```bash
python Test/Test.py
```

## Training Data Format
For effective learning, the training data should be in JSON format with structured intents. Example:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hello", "Hi", "Hey"],
      "responses": ["Hello! How can I assist you?", "Hi there!"]
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you", "Goodbye"],
      "responses": ["Goodbye! Have a great day!", "See you soon!"]
    }
  ]
}
```

Ensure your data follows this structure for optimal performance.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Make your changes.
3. Submit a Pull Request.

## Contact
For questions or suggestions, reach out via email or open an issue on GitHub.
