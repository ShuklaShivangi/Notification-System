from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, SessionLocal
from . import models, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post("/notifications", response_model=schemas.NotificationResponse)
def create_notification(data: schemas.NotificationCreate, db: Session = Depends(get_db)):
    new_notification = models.Notification(
        message=data.message,
        is_read=False
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification


# READ
@app.get("/notifications", response_model=list[schemas.NotificationResponse])
def get_notifications(db: Session = Depends(get_db)):
    return db.query(models.Notification).all()


# UPDATE
@app.put("/notifications/{id}", response_model=schemas.NotificationResponse)
def mark_as_read(id: int, db: Session = Depends(get_db)):
    notification = db.query(models.Notification).filter(models.Notification.id == id).first()
    if notification:
        notification.is_read = True
        db.commit()
        db.refresh(notification)
        return notification
    return {"error": "Not found"}


# DELETE
@app.delete("/notifications/{id}")
def delete_notification(id: int, db: Session = Depends(get_db)):
    notification = db.query(models.Notification).filter(models.Notification.id == id).first()
    if notification:
        db.delete(notification)
        db.commit()
        return {"message": "Deleted"}
    return {"error": "Not found"}