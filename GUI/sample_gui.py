from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

# Create a class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button = QPushButton("Press me!")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        container = QWidget()

        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_click(self):
        print("Button was clicked!")

# Create the application instance
app = QApplication([])
window = MainWindow()
window.show()
