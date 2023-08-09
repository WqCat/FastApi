import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from tutorial import app03, app04 ,app05

app = FastAPI()

# mount表示将某个目录下一个完全独立的应用挂载过来，这个不会在API交互文档中显示
app.mount(path="/static", app=StaticFiles(directory='./coronavirus/static', name='static')) # .mount()不要在分路由APIRouter().mount()调用，模板会报错

app.include_router(app03, prefix='/chapter03', tags=['第三章 请求参数和验证'])
app.include_router(app04, prefix='/chapter04', tags=['第四章 响应处理和FastAPI配置'])
app.include_router(app05, prefix='/chapter05', tags=['第五章 FastAPI的依赖注入系统'])

if __name__ == '__main__':
    uvicorn.run('run:app', host='127.0.0.1', port=8000, reload=True, workers=1)

