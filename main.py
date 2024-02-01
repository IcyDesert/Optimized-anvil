from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='src/template/')


# 挂载，事实上就是挂载导致了某次接连出404
# mount会把/解析到./src/static，憨憨了
#app.mount("/", StaticFiles(directory="./src/static", html=True))


@app.get("/anvil/{enchant_id}", response_class=HTMLResponse)
async def render_HTML(request: Request, enchant_id: str):
    context= {
        "enchant_id": enchant_id,
        }
    return templates.TemplateResponse(
        request = request,
        name = "index.html",
        context=context,
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)