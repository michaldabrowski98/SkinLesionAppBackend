from tensorflow.keras.models import load_model
import os

MODEL_PATH = "model_resnet50_v2.keras"

class ClassificationModel:
    
    def __init__(self):
        self.model = self._load_model_from_path(MODEL_PATH)

    @staticmethod
    def _load_model_from_path(path):
        model_path = os.path.join(os.path.dirname(__file__), path)
        model = load_model(model_path)
        return model
