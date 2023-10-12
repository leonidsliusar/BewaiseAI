from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from api.v1 import rout

app = FastAPI()
app.include_router(router=rout)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/', response_class=FileResponse)
async def index():
    file_path = Path('./static/index.html')
    return FileResponse(file_path)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
