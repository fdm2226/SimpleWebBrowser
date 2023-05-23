from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser():

    def open_bookmarks_window(self):
        QMessageBox.information(self.window, "Bookmarks", "This is the bookmarks window")

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Ciscos Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.tab_widget = QTabWidget()  # Add a tab widget
        self.tab_widget.tabBar().setMovable(True)  # Allow tabs to be moved
        self.tab_widget.setTabsClosable(True)  # Allow tabs to be closed
        self.tab_widget.tabCloseRequested.connect(self.remove_tab)  # Connect tab closing signal to remove_tab method

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.tab_btn = QPushButton("+")
        self.tab_btn.setMinimumHeight(30)

        self.bookmark_btn = QPushButton("Bookmarks")  # Add a bookmarks button

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.tab_btn)
        self.horizontal.addWidget(self.bookmark_btn)  # Add the bookmarks button to the layout


        self.tab_btn.clicked.connect(self.add_new_tab)
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))

        self.bookmark_btn.clicked.connect(self.open_bookmarks_window)  # Connect the bookmarks button to the bookmarks window

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.tab_widget)  # Add tab widget to layout

        self.add_new_tab()  # Add initial tab
        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.tab_widget.currentWidget().setUrl(QUrl(url))  # Set url for current tab

    def add_new_tab(self):
        new_browser = QWebEngineView()
        self.tab_widget.addTab(new_browser, "New Tab")  # Add new tab to tab widget
        new_browser.load(QUrl("http://google.com"))
        self.tab_widget.setCurrentWidget(new_browser)  # Set current widget to the new tab

    def remove_tab(self, index):
        widget = self.tab_widget.widget(index)
        widget.deleteLater()  # Delete widget
        self.tab_widget.removeTab(index)  # Remove tab from tab widget

app = QApplication([])
window = MyWebBrowser()
app.exec_()