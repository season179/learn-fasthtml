from fasthtml.common import *

app = FastHTML()

@app.get("/")
def home():
    page = Html(
        Head(Title("Some page")),
        Body(Div("Hello world!")),
    )
    
    return page

serve()
