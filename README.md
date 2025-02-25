## Software Engineer Chatbot

An AI-powered chatbot designed for software engineers, leveraging OpenAI's Whisper for speech-to-text and ElevenLabs for text-to-speech. Built with Python (backend) and React (frontend).

### Tech Stack
#### Backend
- Python
- API's:
  - OpenAI Whisper – Speech-to-text conversion
  - ElevenLabs – Text-to-speech synthesis
#### Frontend
- React (JavaScript
- NextJS

### Getting Started

1. Clone the Repository
```sh
git clone https://github.com/your-username/software-engineer-chatbot.git
cd software-engineer-chatbot
```
2. Install Dependencies
Frontend
```sh
cd frontend
npm install
```
Backend
```sh
cd ../backend
pip install -r requirements.txt
```
3. Configure API Keys
Create a .env file inside the backend/ directory and add your API keys:
```sh 
OPEN_AI_ORG=your_openai_org
OPEN_AI_KEY=your_openai_api_key
ELEVEN_LABS_API_KEY=your_elevenlabs_api_key
```
4. Run the Application
Open two terminals:
##### Start the Backend (Python Server)
```sh cd backend
python app.py
```

##### Start the Frontend (React App)
```sh
cd frontend
npm start
```
### Features
✅ Convert speech to text using OpenAI's Whisper
✅ Generate AI-powered responses
✅ Convert AI responses to speech using ElevenLabs
✅ Interactive UI for seamless user experience

### Contributing
Feel free to fork the repository, submit issues, or contribute improvements via pull requests.

