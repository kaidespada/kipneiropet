import os 
import shutil
from ultralytics import YOLO

# Переподготовка датасета под 0 - 5

class MNISTSubsetPrepared:


    def __init__(self, dataset_name: str = "mnist"):

        self.dataset_name = dataset_name

        # Папка с подготовленным датасетом
        self.dataset_dir = os.path.join(
            ".", "data", dataset_name
        )

        # Временная папка для оригинального MNIST
        self.raw_dir = os.path.join(
            ".", "data", "raw"
        )

    
    def prepare(self):

        print("Подготовка к скачиванию")

        if self.is_dataset_ready():
            print("Датасет уже подготовлен")
            return

    
        self._create_directories()

        self._download_mnist()

        self._convert_dataset()

        self._remove_extra_classes()

        self._remove_raw_dataset()

        print("Датасет подготовлен")


    def _is_dataset_ready(self):

        # Проверка вообще на наличие датасета

        train_dir = os.path.join(
            self.dataset_dir,
            "train"
        )

        test_dir = os.path.join(
            self.dataset_dir,
            "test"
        )

        if not os.path.exists(train_dir):
            return False

        if not os.path.exists(test_dir):
            return False

        for digit in ["0", "1", "2", "3", "4", "5"]:

            train_class = os.path.join(
                train_dir,
                digit
            )

            test_class = os.path.join(
                test_dir,
                digit
            )

            if not os.path.exists(train_class):
                return False

            if not os.path.exists(test_class):
                return False

        return True


    def _create_directories(self):

        os.makedirs(
            self.dataset_dir,
            exist_ok=True
        )

        os.makedirs(
            self.raw_dir,
            exist_ok=True
        )
    

    def _download_mnist(self):

        # Загрузка MNIST через tortchvision

        print("Скачивание MNIST")

        datasets.MNIST(
            root=self.raw_dir,
            train=True,
            download=True
        )

        datasets.MNIST(
            root=self.raw_dir,
            train=False,
            download=True
        )

        print("MNIST скачан")

    
    def _convert_dataset(self):

        # Работа с MNIST под YOLO Classification

        print("Преобразование датасета под стандарты YOLO")

        
        train_dataset = datasets.MNIST(
            root=self.raw_dir,
            train=True,
            download=False
        )

        test_dataset = datasets.MNIST(
            root=self.raw_dir,
            train=False,
            download=False
        )

        self._save_split(
            train_dataset,
            "train"
        )

        self._save_split(
            test_dataset,
            "test"
        )

    
    def __save_split(self, dataset, split_name: srt):

        split_dir = os.path.join(
            self.dataset_dir,
            split_name
        )

        for index in range(len(dataset)):

            image, label = dataset[index]

            # Оставляем только цифры 0-5
            if label > 5:
                continue

            class_dir = os.path.join(
                split_dir,
                str(label)
            )

            os.makedirs(
                class_dir,
                exist_ok=True
            )

            image_path = os.path.join(
                class_dir,
                f"{index}.png"
            )

            image.save(image_path)

        print(
            f"Часть '{split_name}' готова."
        )


    def _remove_extra_classes(self):

        # Удаление лишних классов (6-9)

        print ("Удаление лишних файлов")

        for split in ["train", "test"]:

            split_dir = os.path.join(
                self.dataset_dir,
                split
            )

            if not os.path.exists(split_dir):
                continue

            for digit in ["6", "7", "8", "9"]:

                digit_dir = os.path.join(
                    split_dir,
                    digit
                )

                if os.path.exists(digit_dir):

                    shutil.rmtree(digit_dir)

                    print(
                        f"Удалена папка: "
                        f"{digit_dir}"
                    )
        

        def _remove_raw_dataset(self):

            if os.path.exists(self.raw_dir):

                shutil.rmtree(
                    self.raw_dir
                )

            print("Временные файлы удалены")


            
            
        