RoomSync AI
AI-assisted roommate discovery and compatibility matching platform

RoomSync AI (also referred to as CohabitAI in parts of the codebase) helps people discover potential roommates by comparing lifestyle preferences, personality traits, budget constraints, and location. It combines a weighted compatibility-scoring engine with profile management, search, comparison, map-based discovery, and a conversational assistant.

Features
- User accounts and profiles — registration, login, profile editing, and roommate preferences.
- Compatibility scoring — compares ten lifestyle and personality dimensions using weighted cosine similarity and weighted Euclidean similarity, with an optional biography-text similarity component.
- Search and discovery — ranks potential matches and applies hard-constraint checks.
- Compare tool — shows areas of alignment and potential friction between users.
- Location-aware discovery — uses geographic coordinates and the Haversine distance calculation for distance-based matching and map results.
- Chat assistant — provides roommate-search guidance and conflict-discussion prompts.
- Questionnaire and local datasets — includes scripts and supporting files for questionnaire/data generation and local development.

- How compatibility is calculated
Each profile is represented by ten preference dimensions, generally scored from 1 to 5:
| Dimension | Weight |
|---|---:|
| Sleep schedule | 5.0 |
| Cleanliness | 5.0 |
| Noise tolerance | 4.5 |
| Introversion / extroversion | 4.0 |
| Social battery | 4.0 |
| Communication style | 3.5 |
| Guest frequency | 3.5 |
| Conflict resolution | 3.0 |
| Cooking frequency | 2.0 |
| Workout habit | 1.5 |

The scoring engine in compatibility.py blends the component scores as follows:
- 60% weighted cosine similarity
- 25% weighted Euclidean similarity
- 15% biography-text similarity (TF-IDF when available)
The result is a compatibility score from 0 to 100. When either biography is missing, the text component uses a neutral score. The implementation also includes hard-constraint checks, nearest-neighbour indexing, feature-level differences, and Haversine distance utilities.

Tech stack
Backend
- Python 
- Flask
- Flask-Login
- Flask-SQLAlchemy
- NumPy
- scikit-learn
- PyMongo (for MongoDB-related workflows)
- python-dotenv
- Requests
Frontend
- React
- React Router
- Bootstrap and Bootstrap Icons
- Chart.js
- Leaflet
The repository includes both Flask/Jinja templates (templates/ and static/) and a React application (frontend/).

Repository structure
RoomSync-AI/
├── app.py                         # Flask application and routes
├── compatibility.py               # Compatibility and matching algorithms
├── chatbot.py                     # Conversational assistant logic
├── models.py                      # SQLAlchemy data models
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment configuration
├── local_data/                    # Local JSON data and question pool
├── templates/                     # Flask/Jinja HTML templates
├── static/                        # Static assets for Flask templates
├── frontend/                      # React frontend application
├── Ideas and Dataset Synthesis/   # Dataset and experimentation utilities
├── generate_ai_questions.py       # Questionnaire generation utility
├── generate_wb_dataset.py         # West Bengal dataset generation utility
├── push_to_mongo.py               # MongoDB data import utility
└── REFERENCES.md                  # Technical references

Getting started
1. Prerequisites
Install:
- Python 3.10 or newer
- Node.js and npm (only if you plan to work on the React frontend)
- Git
2. Clone the repository
  git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
3. Create and activate a virtual environment
Windows (PowerShell):python -m venv .venv
.venv\Scripts\Activate.ps1
4. Install Python dependencies
  pip install -r requirements.txt
5. Configure environment variables
Create a local .env file from the example:

Windows:
Copy-Item .env.example .env

macOS / Linux:
cp .env.example .env
Review .env and set values appropriate for your environment. In particular:
- Set a strong, private SECRET_KEY before using the app beyond local development.
- USERS_FILE_PATH can be set to the JSON user-data file you want the app to use. The application defaults to local_data/users_local_balanced.json.
- OLLAMA_URL and GEMMA_MODEL are used by the local question-generation configuration.
- GEMINI_API_KEY and GEMINI_MODEL are optional alternatives for Google Gemini-based question generation.
- MONGODB_URI is optional for MongoDB-related workflows.
Do not commit .env, API keys, database credentials, or real user data.

6. Run the Flask application
From the repository root:
python app.py

Configuration notes
The supplied .env.example documents the available configuration variables. The application also contains development defaults in its source code, so review the configuration and replace development secrets before deployment. Environment-variable names used by individual scripts may differ; consult the relevant script before configuring a production environment.

Security and privacy
- Never publish a populated .env file or secrets.
- Do not upload real personal information, passwords, phone numbers, precise location data, or private chat history.
- Review the files in local_data/ and Ideas and Dataset Synthesis/ before making the repository public. Replace or remove any data that is not synthetic or explicitly approved for publication.
- Use a production-grade secret key and appropriate database/security settings before deployment.
- The included local JSON files are intended for development/data workflows, not as a production database strategy.

License
No license file was present in the supplied project archive. Unless you add a license, all rights remain with the copyright holder and others do not automatically receive permission to reuse, modify, or distribute this project. Add a LICENSE file if you intend to publish it as open source.
