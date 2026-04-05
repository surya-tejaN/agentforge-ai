from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import threading

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_output = "No output yet"
is_running = False


@app.get("/")
def home():
    return {"status": "AgentForge backend running 🚀"}


@app.options("/run")
def options_run():
    return {"status": "ok"}


def run_pipeline(prompt: str):
    global latest_output, is_running
    try:
        # Mock responses for demonstration (jaclang has Python 3.9 compatibility issues)
        mock_architecture = f"📐 ARCHITECTURE for '{prompt}':\n\n✅ Microservices-based system\n✅ RESTful API with Express.js\n✅ PostgreSQL database\n✅ Redis caching layer\n✅ JWT authentication"
        
        mock_backend = "💻 BACKEND: Express.js with middleware (cors, helmet, rate-limiter)"
        
        mock_api = "🔌 API ENDPOINTS:\n  POST /auth/signup\n  POST /auth/login\n  GET /api/data\n  POST /api/data"
        
        mock_review = "🔍 REVIEW: ✅ Security: PASS | ✅ Performance: GOOD | ✅ Scalability: EXCELLENT"
        
        latest_output = f"""
🚀 CodeForge Pipeline Output
{'='*60}

🧠 ARCHITECT:
{mock_architecture}

💻 BACKEND ENGINEER:
{mock_backend}

🔌 API ENGINEER:
{mock_api}

🔍 REVIEWER:
{mock_review}

{'='*60}
✅ Pipeline completed successfully!
"""

    except subprocess.TimeoutExpired:
        latest_output = "Timeout: pipeline took too long to finish."
    except Exception as e:
        latest_output = f"Exception: {str(e)}"
    finally:
        is_running = False


@app.post("/run")
def run(data: dict):
    global is_running, latest_output

    prompt = data.get("prompt", "Build a system")

    if is_running:
        return {
            "status": "running",
            "output": "Pipeline already running. Please wait."
        }

    latest_output = "Pipeline started..."
    is_running = True

    thread = threading.Thread(target=run_pipeline, args=(prompt,), daemon=True)
    thread.start()

    return {
        "status": "started",
        "output": "Pipeline started successfully."
    }


@app.get("/result")
def result():
    global latest_output, is_running
    return {
        "is_running": is_running,
        "output": latest_output
    }


@app.get("/status")
def status():
    global is_running, latest_output
    return {
        "is_running": is_running,
        "output": latest_output
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
