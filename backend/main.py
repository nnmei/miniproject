from fastapi import FastAPI, Request, UploadFile, File
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import mysql.connector
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import shutil
import time
from line import send_line

load_dotenv()

def get_db_connection():
    cnx = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_user"),
        database=os.getenv("MYSQL_DATABASE")
    )
    return cnx

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# รูป
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    filename = f"{int(time.time())}_{file.filename}"
    filepath = f"static/{filename}"
    with open(filepath, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"url": f"/{filepath}"}

class Pets(BaseModel):
    name: str
    detail: str
    coverimage: str
    latitude: float
    longitude: float

@app.post('/losts')
def create_losts(losts: Pets):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = '''
    INSERT INTO losts (name, detail, coverimage, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (losts.name, losts.detail, losts.coverimage, losts.latitude, losts.longitude))
    cnx.commit()
    losts_id = cursor.lastrowid
    cursor.close()
    cnx.close()
    send_line(f"แจ้งสัตว์หาย: {losts.name} ({losts.detail})")
    return {"id": losts_id}

@app.post('/founds')
def create_founds(founds: Pets):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = '''
    INSERT INTO founds (name, detail, coverimage, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (founds.name, founds.detail, founds.coverimage, founds.latitude, founds.longitude))
    cnx.commit()
    founds_id = cursor.lastrowid
    cursor.close()
    cnx.close()
    send_line(f"พบสัตว์พลัดหลง: {founds.name} ({founds.detail})")
    return {"id": founds_id}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/hello')
def read_hello():
    return {"message": "Hello"}

@app.get('/items/{id}')
def read_item(id: int):
    return {"item": id}

@app.get("/home", include_in_schema=False)
def read_home(request: Request):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM founds ORDER BY id DESC LIMIT 3")
    founds = []
    for row in cursor.fetchall():
        founds.append({
            "id": row[0],
            "name": row[1],
            "detail": row[2],
            "coverimage": row[3],
            "latitude": row[4],
            "longitude": row[5]
        })

    cursor.execute("SELECT * FROM losts ORDER BY id DESC LIMIT 3")
    losts = []
    for row in cursor.fetchall():
        losts.append({
            "id": row[0],
            "name": row[1],
            "detail": row[2],
            "coverimage": row[3],
            "latitude": row[4],
            "longitude": row[5]
        })
    cursor.close()
    cnx.close()
    return templates.TemplateResponse(request, "home.html", {"founds": founds, "losts": losts})

@app.get("/contact", include_in_schema=False)
def read_contact(request: Request):
    return templates.TemplateResponse(request, "contact.html")

@app.get("/form", include_in_schema=False)
def read_form(request: Request):
    return templates.TemplateResponse(request, "form.html")

@app.get("/founds", include_in_schema=False)
def read_founds(request: Request):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM founds ORDER BY id DESC"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()

    founds = []
    for row in rows:
        founds.append({
            "id": row[0],
            "name": row[1],
            "detail": row[2],
            "coverimage": row[3],
            "latitude": row[4],
            "longitude": row[5]
        })

    return templates.TemplateResponse(request, "founds.html", {"founds": founds})

@app.get("/losts", include_in_schema=False)
def read_losts(request: Request):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM losts ORDER BY id DESC"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()

    losts = []
    for row in rows:
        losts.append({
            "id": row[0],
            "name": row[1],
            "detail": row[2],
            "coverimage": row[3],
            "latitude": row[4],
            "longitude": row[5]
        })

    return templates.TemplateResponse(request, "losts.html", {"losts": losts})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)