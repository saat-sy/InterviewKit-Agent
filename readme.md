# InterviewKit Agent

An intelligent AI-powered interview assistant built with LangGraph that conducts structured technical interviews by analyzing resumes and job descriptions to create personalized interview plans.

## Features

- **Resume Processing**: Automatically processes and analyzes candidate resumes
- **Dynamic Planning**: Creates personalized interview plans based on job requirements
- **Adaptive Workflow**: Real-time replanning based on interview progress
- **Technical Assessment**: Conducts technical interviews with contextual questions
- **Feedback System**: Provides comprehensive feedback and final reports
- **Modular Architecture**: Built with LangGraph for scalable workflow management
- **LiveKit Integration**: Real-time voice/video interview capabilities with AI agents
- **Multi-Modal Support**: Text and voice-based interview interactions

## Architecture

The system is built using a multi-layered architecture with LangGraph workflows:

### Core Components

- **Interview Workflow**: Main orchestration layer
- **Step Workflow**: Individual interview step execution
- **State Management**: Typed states for workflow coordination
- **AI Models**: LLM integration for intelligent responses

### Workflow Structure

```
Resume Input → Processing → Planning → Interview Steps → Replanning → Final Report
```

## Project Structure

```
InterviewKit-Agent/
├── agent/
│   ├── models/          # Pydantic models for data structures
│   │   ├── plan.py      # Interview plan model
│   │   ├── step.py      # Interview step model
│   │   ├── question.py  # Question model
│   │   └── ...
│   ├── nodes/           # LangGraph nodes (business logic)
│   │   ├── interview_nodes.py
│   │   └── step_nodes.py
│   ├── prompts/         # AI prompt templates
│   │   ├── interview_prompts.py
│   │   └── step_prompts.py
│   ├── states/          # Workflow state definitions
│   │   ├── interview_state.py
│   │   └── step_state.py
│   ├── utils/           # Utility functions
│   │   ├── llm_provider.py
│   │   └── graph_renderer.py
│   └── workflows/       # LangGraph workflow definitions
│       ├── interview_workflow.py
│       └── step_workflow.py
├── livekit_config/      # LiveKit integration (optional)
│   ├── main.py          # LiveKit agent entry point
│   ├── constants.py     # Sample resume and job data
│   ├── langgraph_livekit_agents.py  # LangGraph-LiveKit adapter
│   └── typedlivekit.py  # Typed LiveKit utilities
├── langgraph.json       # LangGraph configuration
├── requirements.txt     # Python dependencies
└── README.md
```

## Installation

### Prerequisites

- Python 3.8+
- pip or poetry for dependency management

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/saat-sy/InterviewKit-Agent.git
   cd InterviewKit-Agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   # Required: Choose your LLM provider
   GROQ_API_KEY=your_groq_api_key_here
   # OR
   GOOGLE_API_KEY=your_google_api_key_here
   
   # Optional: Additional configuration
   LANGSMITH_API_KEY=your_langsmith_key  # For tracing
   
   # LiveKit Configuration (for voice/video interviews)
   LIVEKIT_URL=wss://your-livekit-server.com
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   
   # Speech Services (for LiveKit)
   DEEPGRAM_API_KEY=your_deepgram_key    # Speech-to-Text
   CARTESIA_API_KEY=your_cartesia_key    # Text-to-Speech
   ```

## Usage

### Basic Usage

```python
from agent.agent import graph

# Prepare interview state
interview_state = {
    "raw_resume": "candidate_resume_text",
    "raw_job_description": "job_description_text",
    "duration": 45,  # minutes
    "interview_start_time": datetime.now(),
    "interview_completed": False,
    "executed_steps": [],
    "overall_feedback": []
}

# Run the interview workflow
result = await graph.ainvoke(interview_state)
print(result["final_report"])
```

### Running with LangGraph CLI

```bash
# Start the LangGraph server
langgraph up

# The graph will be available at http://localhost:8123
```

### Voice/Video Interviews with LiveKit

For real-time voice and video interview capabilities:

1. **Start the LangGraph server**
   ```bash
   langgraph up --port 2024
   ```

2. **Run the LiveKit agent**
   ```bash
   python livekit_config/main.py start
   ```

The agent supports real-time speech-to-text, text-to-speech, and noise cancellation.

## Configuration

### LLM Provider

The system supports multiple LLM providers. Configure in `agent/utils/llm_provider.py`:

```python
def get_llm():
    # Groq (default)
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    # Google Gemini (alternative)
    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    
    return llm
```

### Workflow Customization

Modify workflows in the `agent/workflows/` directory to customize interview flow and behavior.

## State Management

### Interview State

The main workflow state includes:
- `raw_resume`: Original resume text
- `raw_job_description`: Job posting details
- `processed_resume`: AI-processed resume
- `plan`: Current interview plan
- `executed_steps`: Completed interview steps
- `final_report`: Generated assessment report

### Step State

Individual interview steps maintain:
- Current step details
- Responses and feedback
- Progress tracking

## Extensions

### LiveKit Integration

Real-time voice and video interview capabilities with speech-to-text, text-to-speech, and noise cancellation features.

### Custom Nodes

Add custom interview nodes by creating functions in `agent/nodes/` and updating workflow definitions.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [LangGraph](https://langchain-ai.github.io/langgraph/) for workflow orchestration
- Powered by [Groq](https://groq.com/) for fast LLM inference
- Real-time capabilities via [LiveKit](https://livekit.io/) platform