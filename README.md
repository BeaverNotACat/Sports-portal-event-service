# ghidra-event-service
Event service for International Sports Portal Demo. Made for project school
> [!IMPORTANT]  
> This repo is mirrored from [gitlab](https://gitlab.com/hydra-sports-portal/hydra-backend/event-service)
## Stack
- fastapi      API
- pydantic     Schemas serialisation
- sqlalchemy   PostgreSQL ORM
## Project structure
```
    ├── api
    │   └── ...       API routing
    ├── app.py        App root
    ├── database
    │   └── ...       Models, repos, S3
    ├── schemas
    │   └── ...       Serialisation schemas
    ├── service
    │   └── ...       App logics
    ├── settings.py   Pydantic settings shema
    └── utils
        └── ...       Utility modules and interfaces
```
