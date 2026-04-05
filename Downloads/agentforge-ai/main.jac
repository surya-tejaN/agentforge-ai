import sys;
import subprocess;

node Project {
    has request: str;
    has architecture: str = "";
    has backend: dict = {};
    has api: dict = {};
    has review: str = "";
}

walker CodeForge {

    can start with Root entry {
        req = sys.argv[1] if len(sys.argv) > 1 else "Build a blog API with JWT authentication";

        proj = Project(request=req);
        root ++> proj;

        visit proj;
    }

    can run_pipeline with Project entry {

        # 🧠 AGENT 1: ARCHITECT (REAL AI via Backboard)
        print("🧠 [Architect] Analyzing requirements...");
        
        result = subprocess.run(
            ["python", "run_architect.py", here.request],
            capture_output=True,
            text=True
        );
        
        here.architecture = result.stdout.strip();

        report {
            "agent": "Architect (AI)",
            "output": here.architecture
        };

        # 💻 AGENT 2: BACKEND ENGINEER (Structured)
        print("💻 [Backend] Generating server code...");
        
        here.backend = {
            "framework": "Node.js + Express",
            "features": ["middleware", "routing", "error handling"],
            "based_on": here.architecture
        };

        report {
            "agent": "Backend Engineer",
            "output": here.backend
        };

        # 🔌 AGENT 3: API ENGINEER (Structured)
        print("🔌 [API] Creating endpoints...");
        
        here.api = {
            "auth": "JWT",
            "routes": ["POST /login", "POST /signup", "GET /protected"],
            "middleware": ["cors", "helmet", "rate-limiter"],
            "based_on": here.backend
        };

        report {
            "agent": "API Engineer",
            "output": here.api
        };

        # 🔍 AGENT 4: REVIEWER (REAL AI via Backboard)
        print("🔍 [Reviewer] Analyzing system...");
        
        code_summary = "Architecture: " + here.architecture + " | Backend: Express | API: JWT auth";
        
        result2 = subprocess.run(
            ["python", "run_reviewer.py", code_summary],
            capture_output=True,
            text=True
        );
        
        here.review = result2.stdout.strip();

        report {
            "agent": "Reviewer (AI)",
            "output": here.review
        };

        print("\n✅ CodeForge pipeline complete!");
    }
}

with entry {
    print("============================================================");
    print("🚀 AgentForge AI - Multi-Agent System");
    print("============================================================\n");
    
    result = root spawn CodeForge();
    
    print("\n============================================================");
    print("📊 Agent Outputs:");
    print("============================================================");
    print(result.reports);
}
