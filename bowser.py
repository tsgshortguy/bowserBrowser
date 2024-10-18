import sys
import os  # Import os module
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Bowser(QMainWindow):
    def __init__(self):
        super(Bowser, self).__init__()
        self.browser = QWebEngineView()
        
        # Get the absolute path to home.html
        self.home_url = QUrl.fromLocalFile(os.path.abspath('home.html'))
        self.browser.setUrl(self.home_url)
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Apply the fiery theme using style sheets
        self.setStyleSheet("""
        QMainWindow {
            background: qlineargradient(
                spread:pad,
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #FF4500,
                stop:0.5 #FF8C00,
                stop:1 #FFD700
            );
        }
        QToolBar {
            background: transparent;
            padding: 5px;
        }
        QToolButton {
            background-color: #8B0000;
            color: white;
            border: 1px solid #FFD700;
            padding: 5px;
            border-radius: 5px;
            margin: 2px;
        }
        QToolButton:hover {
            background-color: #FF0000;
        }
        QLineEdit {
            background-color: #FFFFE0;
            color: #8B0000;
            border: 1px solid #FFD700;
            padding: 5px;
            border-radius: 5px;
        }
        """)

        # Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(self.home_url)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://', 'file://')):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Bowser')
window = Bowser()
app.exec_()
