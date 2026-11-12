
# Country Quiz 

Country Quiz is a Python terminal-based quiz game that uses live country data from the REST Countries API.

The game asks random questions about country capitals and currencies. Each question has four options, and your final score is displayed at the end.

## Features

- Fetches live country data from an API.
- Random capital and currency questions.
- Four multiple-choice options.
- Score tracking.
- 10 questions per game.

## Technologies Used

- Python
- Requests
- Python-dotenv
- REST Countries API

## Installation

1. Clone this repository:

```bash
git clone https://github.com/shakirhussain3007/Country-Quiz.git
```

2. Open the project folder:

```bash
cd Country-Quiz
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate
```

5. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## API Key Setup

1. Copy `.env.example` and rename the copy to `.env`.
2. Add your REST Countries API key inside `.env`:

```env
API_KEY=your_api_key_here
```

Never upload your real API key to GitHub.

## Run the Project

```bash
python main.py
```

## Sample Output

See [sample_output.txt](sample_output.txt) for an example of the quiz output.

## Author

Shakir Hussain
