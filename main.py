from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.dependencies.index_context import index_context_shared
from src.services import core


app = FastAPI()
app.include_router(core.checker_sorter)
app.mount("/static", StaticFiles(directory="./src/static"), name="static", )

templates = Jinja2Templates(directory='src/template/')

@app.get("/anvil/", response_class=HTMLResponse)
async def render_HTML(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=index_context_shared,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
