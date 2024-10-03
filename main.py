from fasthtml.common import *

app = FastHTML(hdrs=(picolink))

@app.get("/")
def home():
    # page = Html(
    #     Head(Title("Some page")),
    #     Body(Main(Div("Hello world!"))),
    # )
    page = (Title("A Title"),
            Main(Div("Hello world!")))
    
    return page

serve()
