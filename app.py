from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"massege":"theek ho gaya ha "}

posts = {'title':"ehsas", 'discription':"just join it"}
@app.get("/posts")
def get_posts():
    return posts