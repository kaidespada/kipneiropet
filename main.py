from src.dataset import MNISTSubsetPrepared
from src.model import MNISTModel


def main():

    print("=" * 50)
    print("MNIST YOLO PROJECT")
    print("=" * 50)

    # Создаём объект подготовки датасета
    dataset = MNISTSubsetPrepared(
        dataset_name="mnist"
    )

    # Подготавливаем датасет
    dataset.prepare()

    # Показываем статистику
    dataset.print_statistics()

    # Создаём модель
    model = MNISTModel(
        model_name="yolo11n-cls.pt"
    )

    # Обучаем модель
    model.train(
        data_dir="./data/mnist",
        epochs=10,
        image_size=32
    )


if __name__ == "__main__":
    main()