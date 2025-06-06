from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.info import Info
from api.author.author_api import router as authors_router
from api.book.book_api import router as books_router
from api.tvarv.tvarv_api import router as tvarv_router
from api.api_details.api_details import router as api_details_router

app = FastAPI(servers=[
        {"url": "https://testapi-006v.onrender.com"}
    ])
app.include_router(authors_router, prefix="/authors")
app.include_router(books_router, prefix="/books")
app.include_router(tvarv_router, prefix="/tvarv")
app.include_router(api_details_router, prefix="/api_details")

app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )


@app.get("/", response_model=Info)
def info() -> Info:
    info = Info(info="Sample OpenAPI Specification")
    return info


async def root():
    return {"message": "Test"}
