# resume_analyzer
resume_analyzer/
│── backend/        # Flask API (Python)
│   ├── app.py      # Main Flask app
│   ├── requirements.txt  # Dependencies
│   ├── utils/      # Helper functions
│   ├── models/     # ML models for parsing
│   └── uploads/    # Uploaded resumes (PDFs)
│
│── frontend/       # React UI (Vite + Tailwind)
│   ├── src/        # React source code
│   │   ├── components/  # UI components
│   │   ├── pages/       # Main pages
│   │   ├── App.jsx      # Main React component
│   │   └── main.jsx     # Entry point
│   ├── public/     # Static assets
│   ├── package.json # Frontend dependencies
│   ├── vite.config.js # Vite configuration
│   └── index.html   # Entry HTML file
│
│── models/         # ML Models (NLP for Resume Parsing)
│   ├── nlp_model.pkl
│   ├── text_extraction.py
│   ├── experience_extraction.py
│   └── education_extraction.py
│
│── data/           # Sample Resume Files
│   ├── sample1.pdf
│   ├── sample2.docx
│   └── sample3.txt
│
│── .gitignore      # Ignore unnecessary files
│── README.md       # Project documentation
│── requirements.txt # Python dependencies
└── package.json    # Frontend dependencies
