from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.model import enchantments_list as enct
from src.model import items_list as items
# from src.model.response import Enchant_response
# from src.model.request import Enchant_request

app = FastAPI()
templates = Jinja2Templates(directory='src/template/')


@app.get("/anvil/", response_class=HTMLResponse)
async def render_HTML(request: Request) -> None:
    context = {
        "item_universal": enct.item_universial,
        "armor_universal": enct.armor_universal,
        "armor_specific": enct.armor_specific,
        "tool_universal": enct.tool_universal,
        "sword_specific": enct.sword_specific,
        "bow_specific": enct.bow_specific,
        "armor": items.armor,
        "weapon": items.weapon,
        "tool": items.tool,
    }
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
