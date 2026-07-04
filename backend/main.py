import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import ChatRequest, ChatResponse
from workflow import PsychologistWorkflow

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Psychologist API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = PsychologistWorkflow()


@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "AI Psychologist",
    }


@app.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    logger.info(
        "Received chat request. session=%s",
        request.session_id,
    )

    context, results = workflow.execute(
        session_id=request.session_id,
        message=request.message,
    )

    graph = workflow.engine.get_workflow_graph(results)

    final_response = ""

    if context.state.response:
        final_response = context.state.response.response

    return ChatResponse(
        session_id=request.session_id,
        workflow=results,
        workflow_graph=graph,
        final_response=final_response,
    )