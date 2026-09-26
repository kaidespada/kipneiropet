from src.dataset import MNISTSubsetPrepared
from src.model import MNISTModel
from src.drawing import DrawingWindow

def main():

    print("KIP PET PROJ AI")
    
    # Подготовка датасета
    dataset = MNISTSubsetPrepared(
        dataset_name="mnist"
    )

    dataset.prepare()

    # Создание модели
    model = MNISTModel(
        model_name="yolo11n-cls.pt"
    )

    # Обучение модели
    model.train(
        data_dir="./data/mnist",
        epochs=10,
        image_size=64
    )

    window = DrawingWindow(
        model=model
    )
    window.run()


if __name__ == "__main__":
    main()