from fastapi import FastAPI
import subprocess
import threading

app = FastAPI()

# store results (simple memory)
results = {}

@app.get("/")
def home():
    return {"status": "AgentForge backend running 🚀"}

# background worker
def run_pipeline(job_id, prompt):
    try:
        result = subprocess.run(
            ["python3", "-m", "jaclang", "run", "main.jac", prompt],
            capture_output=True,
            text=True
        )

        results[job_id] = result.stdout if result.stdout else result.stderr

    except Exception as e:
        results[job_id] = str(e)


# start job
@app.post("/run")
def run(data: dict):
    prompt = data.get("prompt", "Build a system")

    job_id = str(len(results) + 1)

    # start in background
    thread = threading.Thread(target=run_pipeline, args=(job_id, prompt))
    thread.start()

    return {
        "status": "started",
        "job_id": job_id
    }


# get result
@app.get("/result/{job_id}")
def get_result(job_id: str):
    if job_id in results:
        return {
            "status": "completed",
            "output": results[job_id]
        }
    else:
        return {
            "status": "running"
        }