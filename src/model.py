from ultralytics import YOLO


class MNISTModel:

    def __init__(self, model_name: str = "yolo11n-cls.pt"):

        self.model_name = model_name

        print(
            f"[INFO] Загружаем модель "
            f"{self.model_name}..."
        )

        self.model = YOLO(self.model_name)

    def train(
        self,
        data_dir: str = "./data/mnist",
        epochs: int = 10,
        image_size: int = 32
    ):

        print("[INFO] Начинаем обучение...")

        results = self.model.train(
            data=data_dir,
            epochs=epochs,
            imgsz=image_size
        )

        return results

    def predict(self, image_path: str):

        results = self.model.predict(
            source=image_path
        )

        result = results[0]

        class_id = result.probs.top1
        confidence = result.probs.top1conf.item()

        return class_id, confidence