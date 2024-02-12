from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.model.response import Enchant_response
from src.model.request import Enchant_request
from src.services.check import checker_router
app = FastAPI()
templates = Jinja2Templates(directory='src/template/')

app.include_router(checker_router)

@app.get("/anvil", response_class=HTMLResponse)
async def render_HTML(request: Enchant_request, enchant_id: int):
    context= {
        "enchant_id": enchant_id,
        }
    return templates.TemplateResponse(
        request = request,
        name = "index.html",
        context = context,
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)