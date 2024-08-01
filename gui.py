from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QScrollBar, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor
from prompt import get_response

class ChatBotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.context = ""
        self.welcome_message()

    def init_ui(self):
        # Window setup
        self.setWindowTitle('Personal Movie Assistant Chat')
        self.setGeometry(100, 100, 700, 650)

        # Title label
        title_label = QLabel("Personal Movie Assistant")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #4f6f8f;")

        # Chat history area with an attached scrollbar
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setFont(QFont("Arial", 12))
        self.chat_area.setStyleSheet("""
            background-color: #ecf0f1;
            padding: 10px;
            border: 1px solid #bdc3c7;
            color: #2c3e50;
            border-radius: 10px;
            margin: 10px 0px 10px 10px;
        """)
        self.chat_area.setLineWrapMode(QTextEdit.WidgetWidth)

        # Adding a vertical scrollbar
        self.scrollbar = QScrollBar(self)
        self.scrollbar.setOrientation(Qt.Vertical)
        self.chat_area.setVerticalScrollBar(self.scrollbar)
        
        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setStyleSheet("padding: 10px; border: 1px solid #bdc3c7; background-color: #ffffff; color: #2c3e50; border-radius: 5px;")

        # Send button
        self.send_button = QPushButton('Send', self)
        self.send_button.setFont(QFont("Arial", 10))  # Reduced font size
        self.send_button.setStyleSheet("""
            padding: 5px 15px;  # Reduced padding
            border: none;
            background-color: #3498db;
            color: white;
            border-radius: 5px;
        """)
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)

        # Layout setup
        chat_layout = QHBoxLayout()
        chat_layout.addWidget(self.chat_area)
        chat_layout.addWidget(self.scrollbar)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addLayout(chat_layout)
        main_layout.addWidget(self.input_field)
        main_layout.addWidget(self.send_button)
        self.setLayout(main_layout)

    def welcome_message(self):
        welcome_text = (
            "Welcome to your personal movie assistant! 🎬\n\n"
            "I'm here to help you discover and explore the world of movies. Whether you're looking for recommendations, "
            "information about a specific film, or just some interesting trivia, I'm at your service.\n\n"
            "To get started, you can ask me to recommend a movie based on your favorite genre, actor, or director. "
            "You can also ask for detailed information about a particular movie, including its plot, cast, and background details.\n\n"
            "Feel free to type your question in the box below and hit 'Send'. Let's dive into the world of cinema together!"
        )
        self.append_message(welcome_text, user=False)

    def send_message(self):
        user_message = self.input_field.text().strip()
        if user_message:
            # Display user message immediately
            self.append_message(f"You: {user_message}", user=True)
            self.input_field.clear()
            
            # Get response from the chatbot
            bot_response = get_response(self.context, user_message)
            self.context += f"\nUser: {user_message}\nBot: {bot_response}\n"

            # Display bot response in the chat area
            self.append_message(f"Bot: {bot_response}", user=False)
            self.auto_scroll()

    def append_message(self, message, user=True):
        if user:
            formatted_message = f'<p style="color:#2980b9; margin: 10px 0;"><b>{message}</b></p>'  # User message in blue
        else:
            formatted_message = self.format_bot_response(message)
        self.chat_area.append(formatted_message)
        self.auto_scroll()

    def format_bot_response(self, message):
        # Replace Markdown-style bold (**) with HTML bold (<b>)
        message = message.replace('**', '<b>').replace('**', '</b>')

        # Add more line spacing between paragraphs
        lines = message.split('\n')
        formatted_lines = []
        for line in lines:
            if line.strip().startswith('*'):
                # Add bullets for items that start with '*'
                line = f'<li style="margin-bottom: 10px;">{line.replace("*", "").strip()}</li>'
            else:
                # Wrap other lines in paragraphs with a margin
                line = f'<p style="margin-bottom: 10px;">{line.strip()}</p>'
            formatted_lines.append(line)

        # Join lines and wrap in an unordered list if it contains list items
        formatted_message = ''.join(formatted_lines)
        if '<li' in formatted_message:
            formatted_message = f'<ul style="margin-left: 20px; padding-left: 20px;">{formatted_message}</ul>'
        return formatted_message

    def auto_scroll(self):
        cursor = self.chat_area.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.chat_area.setTextCursor(cursor)
        self.chat_area.ensureCursorVisible()

def main():
    app = QApplication([])
    chatbot = ChatBotGUI()
    chatbot.show()
    app.exec_()

if __name__ == '__main__':
    main()