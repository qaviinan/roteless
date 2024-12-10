# Roteless

![Home Screen](./assets/home.png) ![Quiz Screen](./assets/quiz_screen.png)
![Account](./assets/account_screen.png) ![Signin](./assets/signin_screen.png)

*Home screen displaying mnemonic meme feed, quiz screen, and other screens.*

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
    - [Frontend](#frontend)
    - [Backend](#backend)
- [Project Structure](#project-structure)
  - [Frontend Structure](#frontend-structure)
  - [Backend Structure](#backend-structure)
- [Testing](#testing)
  - [Backend Testing](#backend-testing)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

**Roteless** is a comprehensive application designed to enhance vocabulary acquisition by converting memes into mnemonic devices using generative AI. The project consists of two main components:

- **Frontend**: A Flutter-based application that fetches memes from Reddit, incorporates vocabulary into the captions using Large Language Models (LLMs), and presents the content interactively on both Android and Web platforms.
  
- **Backend**: A Python-based system that automates the fetching of memes from Reddit, generates mnemonic captions using OpenAI's GPT-4, and stores the processed posts in Firebase. This backend serves data to the frontend, ensuring a seamless and engaging user experience.

---

## Features

### Frontend
- **Cross-Platform Support**: Runs seamlessly on Android devices and Flutter Web.
- **Generative AI Integration**: Utilizes OpenAI to generate mnemonic captions for memes.
- **Firebase Integration**: Fetches and displays processed meme posts from Firebase.
- **User-Friendly Interface**: Intuitive design for easy navigation and interaction.
- **Real-Time Updates**: Automatically updates with new mnemonic posts without requiring manual refresh.

### Backend
- **Reddit Scraping**: Automatically fetches memes from specified subreddits using PRAW.
- **Generative AI Integration**: Utilizes OpenAI's GPT-4 to create mnemonic captions for memes.
- **Firebase Integration**: Stores and manages processed posts in Firebase Firestore.
- **Duplicate Checking**: Ensures that only new and unique posts are processed and stored.
- **Logging**: Comprehensive logging for monitoring and debugging.
- **Configuration Management**: Centralized configuration for easy adjustments.
- **Modular Architecture**: Organized codebase for maintainability and scalability.
- **Testing**: Unit tests to ensure reliability of individual components.

---

## Screenshots

![Home Screen](./assets/home_screen.png)
*Home screen displaying mnemonic memes.*

![Meme Detail](./assets/meme_detail.png)
*Meme detail view with generated mnemonic.*

---

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements for both Frontend and Backend:

#### Frontend
- **Flutter SDK**: [Install Flutter](https://flutter.dev/docs/get-started/install) (version 3.0 or higher recommended)
- **Dart SDK**: Comes bundled with Flutter
- **Firebase Project**: Set up a Firebase project and obtain the configuration files
- **OpenAI API Key**: Obtain an API key from [OpenAI](https://openai.com/api/)
- **Android Studio or VS Code**: Recommended IDEs for Flutter development
- **Web Browser**: For running the web version

#### Backend
- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Comes bundled with Python
- **Virtual Environment Tool**: `venv`, `pipenv`, or `poetry`
- **Firebase Account**: Set up a Firebase project and obtain service account credentials
- **Reddit API Credentials**: Register an application to obtain `client_id`, `client_secret`, and `user_agent`
- **OpenAI API Key**: Obtain an API key from [OpenAI](https://openai.com/api/)

---

### Installation

#### Clone the Repository

```bash
git clone https://github.com/yourusername/roteless.git
cd roteless
```

#### Frontend Installation

1. **Navigate to Frontend Directory**

   ```bash
   cd frontend/roteless_flutter_app
   ```

2. **Install Dependencies**

   ```bash
   flutter pub get
   ```

3. **Configure Firebase**

   - **Android**:
     - Download the `google-services.json` file from your Firebase project settings.
     - Place it in the `android/app/` directory.

   - **Web**:
     - In your Firebase project settings, locate the Firebase SDK snippet for the web.
     - Replace the placeholder configuration in `lib/firebase_options.dart` with your actual Firebase config.

4. **Configure Environment Variables**

   Create a `.env` file in the root of `roteless_flutter_app` and add your Firebase and OpenAI configurations.

   ```env
   FIREBASE_API_KEY=your_firebase_api_key
   FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
   FIREBASE_PROJECT_ID=your_project_id
   FIREBASE_STORAGE_BUCKET=your_project_id.appspot.com
   FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
   FIREBASE_APP_ID=your_app_id
   OPENAI_API_KEY=your_openai_api_key
   ```

   **Note**: Ensure `.env` is listed in your `.gitignore` to prevent sensitive information from being exposed.

#### Backend Installation

1. **Navigate to Backend Directory**

   ```bash
   cd ../backend
   ```

2. **Set Up a Virtual Environment**

   Using `venv`:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the `backend/` directory and add the following configurations:

   ```env
   # Reddit API Credentials
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=RotelessBot/0.1 by your_username

   # OpenAI API
   OPENAI_API_KEY=your_openai_api_key

   # Firebase
   FIREBASE_CREDENTIALS=path/to/roteless-vgtppm-firebase.json

   # Subreddits to Fetch
   SUBLIST=sub1,sub2,sub3

   # Prompts
   IMAGE_PROMPT=Describe the image: 
   FULL_PROMPT=Generate a caption: 
   ```

5. **Firebase Credentials**

   - Download the `roteless-vgtppm-firebase.json` file from your Firebase project settings.
   - Place it in the `backend/` directory or a secure location of your choice.
   - Update the `FIREBASE_CREDENTIALS` path in the `.env` file accordingly.

---

### Running the Application

#### Frontend

##### Android

1. **Connect an Android Device** or start an Android emulator.

2. **Run the App**

   ```bash
   flutter run
   ```

##### Web

1. **Enable Web Support**

   If not already enabled, run:

   ```bash
   flutter config --enable-web
   ```

2. **Run the App on Web**

   ```bash
   flutter run -d chrome
   ```

#### Backend

1. **Ensure Virtual Environment is Activated**

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Backend**

   ```bash
   python src/main.py
   ```

   **Note**: The `main.py` script is configured to execute the `timed_run` function, which fetches, processes, and uploads posts.

---

## Configuration

### Firebase

Ensure that Firebase is correctly configured for both Frontend and Backend platforms.

- **Frontend**: Refer to the [Firebase Flutter documentation](https://firebase.flutter.dev/docs/overview/) for detailed setup instructions.
  
- **Backend**: Ensure the Firebase credentials (`roteless-vgtppm-firebase.json`) are correctly referenced in the `.env` file.

### OpenAI

- **Frontend**: The frontend interacts with the backend to fetch processed meme posts. Ensure the backend has access to the OpenAI API.
  
- **Backend**: Ensure the OpenAI API key is correctly set in the `.env` file to enable caption generation.

---

## Project Structure

```
roteless/
├── frontend/
│   ├── roteless_flutter_app/
│   │   ├── android/
│   │   ├── ios/
│   │   ├── lib/
│   │   │   ├── models/
│   │   │   ├── services/
│   │   │   ├── screens/
│   │   │   ├── widgets/
│   │   │   ├── main.dart
│   │   │   └── firebase_options.dart
│   │   ├── web/
│   │   ├── assets/
│   │   ├── test/
│   │   ├── pubspec.yaml
│   │   ├── .env
│   │   └── README.md
│   └── README.md
├── backend/
│   ├── src/
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── firebase/
│   │   │   ├── __init__.py
│   │   │   └── firebase_handler.py
│   │   ├── reddit/
│   │   │   ├── __init__.py
│   │   │   └── reddit_client.py
│   │   ├── openai_client/
│   │   │   ├── __init__.py
│   │   │   └── openai_client.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── json_utils.py
│   │   │   └── logger.py
│   │   └── main.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_reddit_client.py
│   │   ├── test_firebase_handler.py
│   │   └── test_openai_client.py
│   ├── requirements.txt
│   ├── .env
│   └── README.md
└── README.md
```

### Frontend Structure

- **android/**: Android-specific configurations and code.
- **ios/**: iOS-specific configurations and code.
- **lib/**: Main Flutter application code.
  - **models/**: Data models.
  - **services/**: Services for data fetching and processing.
  - **screens/**: UI screens.
  - **widgets/**: Reusable UI components.
  - **main.dart**: Entry point of the Flutter application.
  - **firebase_options.dart**: Firebase configuration.
- **web/**: Web-specific configurations and code.
- **assets/**: Image and other asset files.
- **test/**: Frontend tests.
- **pubspec.yaml**: Flutter dependencies.
- **.env**: Environment variables (ensure this is added to `.gitignore`).
- **README.md**: Frontend-specific documentation.

### Backend Structure

- **src/**: Main backend source code.
  - **config/**: Centralized configuration management.
    - `config.py`: Configuration settings.
  - **firebase/**: Firebase interaction logic.
    - `firebase_handler.py`: Handles Firebase operations.
  - **reddit/**: Reddit scraping and data fetching.
    - `reddit_client.py`: Handles Reddit API interactions.
  - **openai_client/**: OpenAI API interactions.
    - `openai_client.py`: Handles OpenAI API requests.
  - **utils/**: Utility modules for JSON handling and logging.
    - `json_utils.py`: JSON utilities.
    - `logger.py`: Logging setup.
  - `main.py`: Entry point for running the backend processes.
- **tests/**: Unit and integration tests for backend modules.
  - `test_reddit_client.py`: Tests for Reddit client.
  - `test_firebase_handler.py`: Tests for Firebase handler.
  - `test_openai_client.py`: Tests for OpenAI client.
- **requirements.txt**: Python dependencies.
- **.env**: Environment variables (ensure this is added to `.gitignore`).
- **README.md**: Backend-specific documentation.

---

## Testing

### Frontend Testing

*Frontend tests are located in the `frontend/roteless_flutter_app/test/` directory.*

To run frontend tests:

```bash
cd frontend/roteless_flutter_app
flutter test
```

### Backend Testing

Backend unit tests are located in the `backend/tests/` directory.

1. **Ensure Virtual Environment is Activated**

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run Tests**

   ```bash
   python -m unittest discover -s tests
   ```

   **Example Output:**

   ```bash
   ...
   ----------------------------------------------------------------------
   Ran 3 tests in 0.123s

   OK
   ```

---

## Logging

### Backend Logging

Logging is implemented using Python’s built-in `logging` module. Logs are stored in `roteless.log` located in the `backend/` directory.

#### Log Levels

- **INFO**: General operational messages.
- **WARNING**: Indications of potential issues.
- **ERROR**: Errors that prevent certain operations from completing.

#### Accessing Logs

View the log file to monitor backend operations and debug issues.

```bash
tail -f backend/roteless.log
```

---

## Contributing

Contributions are highly appreciated! The project comprises both frontend and backend components, so please follow the respective guidelines below.

### General Steps

1. **Fork the Repository**

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/roteless.git
   cd roteless
   ```

3. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

4. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

5. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

6. **Open a Pull Request**

### Frontend Contributions

- Ensure that your code adheres to Flutter's best practices.
- Write unit and widget tests for new features.
- Update the `frontend/roteless_flutter_app/README.md` if necessary.

### Backend Contributions

- Follow Python's PEP 8 style guidelines.
- Write unit tests for new functionalities.
- Update the `backend/README.md` if necessary.

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Contact

For any questions or suggestions, please contact qaviinan@gmail.com
