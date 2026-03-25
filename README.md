# AI Customer Support Platform

AI-powered chatbot platform using LLMs for automated customer support.

## Features
- Real-time chat
- LLM integration
- Scalable backend
- Modular architecture

## Tech Stack
- FastAPI
- Next.js
- OpenAI API
- Docker

## Setup

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend
cd frontend
npm install
npm run dev

## Architecture
- REST API for chat processing
- LLM service abstraction
- Frontend communicates via API

## Future Improvements
- Vector DB integration
- Authentication system
- Admin dashboard
