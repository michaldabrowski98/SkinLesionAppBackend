from sqlalchemy.orm import Session
from typing import List, Optional
import models

def get_skin_lesion_by_code(db: Session, code: str) -> Optional[models.SkinLesion]:
    return db.query(models.SkinLesion).filter(models.SkinLesion.code == code).first()

def get_all_skin_lesions(db: Session) -> List[models.SkinLesion]:
    return db.query(models.SkinLesion).all()
