from celery import Task
from typing import Optional
from celery.utils.log import get_task_logger
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
from .worker import app
import logging
import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np

logger = get_task_logger(__name__)

IMG_SIZE = 299
IMG_CLASSES = ['MEL', 'BCC', 'SCC']
CONFIDENCE_THRESHOLD = 0.5

class PredictTask(Task):
    abstract = True

    def __init__(self) -> None:
        super().__init__()
        self.model: Optional[Model] = None

    def load_model(self) -> Optional[Model]:
        model_path = os.path.join(os.path.dirname(__file__), 'ml', 'model_resnet50_v2.keras')
        try:
            model = load_model(model_path)
            logger.info("Model loaded successfully")
            return model
        except Exception as e:
            logger.error("Error loading model: %s", e)
            return None

    def __call__(self, *args, **kwargs):
        if self.model is None:
            self.model = self.load_model()
        return self.run(*args, **kwargs)

@app.task(ignore_result=False,
          bind=True,
          base=PredictTask,
          name='celery_task_app.tasks.predict_single')
def predict_single(self, image) -> Optional[str]:
    try:
        image_data = base64.b64decode(image)
        image = Image.open(BytesIO(image_data))
        image = image.resize((IMG_SIZE, IMG_SIZE))
        image = np.array(image)
        
        if image.ndim == 2:
            image = np.stack((image,)*3, axis=-1)
        
        image = np.expand_dims(image, axis=0)
        prediction = self.model.predict(image)
        predicted_class_idx = np.argmax(prediction[0])
        confidence = prediction[0][predicted_class_idx]

        if confidence < CONFIDENCE_THRESHOLD:
                return None
        else:
            return IMG_CLASSES[predicted_class_idx]
    except Exception as e:
        logger.error("Error during prediction: %s", e)
        raise e
