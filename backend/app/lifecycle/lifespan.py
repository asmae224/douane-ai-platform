from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application started")

    # Initialisation future :
    # - PostgreSQL
    # - ChromaDB
    # - MCP
    # - Agents IA

    yield

    logger.info("Application stopped")

    # Fermeture future :
    # - Database
    # - Vector DB
    # - Logs