import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QTimer, Qt

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.remaining_time = 60
        self.game_active = False

        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Clicker Game")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.title_label = QLabel("Welcome to Clicker Game!", self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.timer_label = QLabel(f"Time left: {self.remaining_time} sec", self)
        self.timer_label.setStyleSheet("font-size: 18px; color: #555;")
        self.timer_label.setAlignment(Qt.AlignCenter)

        self.score_label = QLabel(f"Score: {self.score}", self)
        self.score_label.setStyleSheet("font-size: 18px; color: #555;")
        self.score_label.setAlignment(Qt.AlignCenter)

        self.high_score_label = QLabel(f"High Score: {self.high_score}", self)
        self.high_score_label.setStyleSheet("font-size: 18px; color: #555;")
        self.high_score_label.setAlignment(Qt.AlignCenter)

        self.start_button = QPushButton("Start Game", self)
        self.start_button.clicked.connect(self.start_game)
        self.start_button.setStyleSheet(self.button_style())

        self.click_button = QPushButton("Click Me!", self)
        self.click_button.clicked.connect(self.click_button_action)
        self.click_button.setStyleSheet(self.button_style())

        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_game)
        self.reset_button.setStyleSheet(self.button_style())

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)

        layout.addSpacing(20)
        layout.addWidget(self.timer_label)
        
        layout.addSpacing(20)
        layout.addWidget(self.score_label)
        
        layout.addSpacing(20)
        layout.addWidget(self.high_score_label)

        layout.addSpacing(30)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.click_button)
        button_layout.addWidget(self.reset_button)

        layout.addLayout(button_layout)

        layout.setAlignment(Qt.AlignCenter)
        
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def button_style(self):
        return """
            QPushButton {
                font-size: 16px;
                background-color: #4CAF50; /* Зеленый фон */
                color: white; /* Белый текст */
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049; /* Темный зеленый при наведении */
            }
            QPushButton:pressed {
                background-color: #388E3C; /* Темный зеленый при нажатии */
            }
        """

    def click_button_action(self):
        if self.game_active:
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")

    def reset_game(self):
        self.score = 0
        self.remaining_time = 60
        self.game_active = False
        self.score_label.setText(f"Score: {self.score}")
        self.timer_label.setText(f"Time left: {self.remaining_time} sec")

    def update_timer(self):
        if self.remaining_time > 0 and self.game_active:
            self.remaining_time -= 1
            self.timer_label.setText(f"Time left: {self.remaining_time} sec")
        else:
            self.end_game()

    def start_game(self):
        if not self.game_active:
            self.game_active = True
            self.score = 0
            self.remaining_time = 60
            self.score_label.setText(f"Score: {self.score}")
            self.high_score_label.setText(f"High Score: {self.high_score}")
            self.timer_label.setText(f"Time left: {self.remaining_time} sec")
            self.timer.start(1000)
            QTimer.singleShot(60000, self.end_game)  

    def end_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.setText(f"High Score: {self.high_score}")
        self.game_active = False
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = ClickerGame()
    game.show()
    sys.exit(app.exec_())
