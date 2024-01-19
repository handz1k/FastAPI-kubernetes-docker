
# FastAPI Web Service with Kubernetes Deployment

## Project Overview
This project is a FastAPI web service integrated with MongoDB, containerized using Docker, and deployed to a Kubernetes cluster. It demonstrates basic CRUD operations, database integration, and cloud-native deployment techniques.

## Key Components
- **FastAPI Application**: Python-based web service for CRUD operations.
- **MongoDB**: NoSQL database for data persistence.
- **Docker**: Containerization of the FastAPI application.
- **Kubernetes**: Orchestration of application and database services using Kubernetes.

## Features
- CRUD Operations: Supports Create, Read, Update, and Delete operations for `course` and `student` data models.
- HTTP Request Handling: Processes requests and returns JSON responses.
- Database Integration: MongoDB used for storing and retrieving data.
- Containerization: Dockerized FastAPI application.
- Kubernetes Deployment: Managed using Kubernetes for application and database services.

## Technical Specifications
- **FastAPI**: Manages web requests and MongoDB communication.
- **MongoDB**: Stores data with predefined schemas for `course` and `student`.
- **Dockerfile**: Defines the FastAPI application environment.
- **Kubernetes Manifests**: `mongo.yaml` and `fastapi.yaml` for service deployments.

## Schemas and Routes
- `Course` Schema: Attributes include `name`, `description`, `tags`, `students`.
- `Student` Schema: Attributes are `name` and `student_number`.
- Routes: Include operations like Create, Read, Update, and Delete for both `course` and `student`.

## Deployment Instructions
- **Docker**: Build the FastAPI application Docker image.
- **Kubernetes**: Apply `mongo.yaml` and `fastapi.yaml` using `kubectl`.

## Usage
- The application listens on port 5000 and interacts with MongoDB.
- Accessible CRUD operations via defined routes.

---

*This project is part of the CS-E4190 Cloud Software and Systems course.*
