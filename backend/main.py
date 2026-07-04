import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import ChatRequest, ChatResponse
from workflow import PsychologistWorkflow

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# FastAPI
# -----------------------------------------------------------------------------

app = FastAPI(
    title="AI Psychologist",
    version="1.0.0",
    description="Multi-Agent AI Psychologist Workflow",
)

# -----------------------------------------------------------------------------
# CORS
# -----------------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# Workflow
# -----------------------------------------------------------------------------

workflow = PsychologistWorkflow()

# -----------------------------------------------------------------------------
# Routes
# -----------------------------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AI Psychologist API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    logger.info(
        "Incoming chat request. session=%s",
        request.session_id,
    )

    try:

        response = workflow.execute(
            session_id=request.session_id,
            message=request.message,
        )

        logger.info(
            "Workflow completed successfully."
        )

        return response

    except Exception as ex:

        logger.exception("Workflow execution failed.")

        raise HTTPException(
            status_code=500,
            detail=str(ex),
        )