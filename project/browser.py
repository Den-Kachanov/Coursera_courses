import sys
import os
from PyQt6.QtCore import (
    QUrl, Qt, QSize, QTimer, QPropertyAnimation,
    QEasingCurve, pyqtSignal, QThread
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QTabWidget,
    QTabBar, QLabel, QProgressBar, QToolBar, QSizePolicy,
    QStatusBar, QMenu, QDialog, QListWidget, QListWidgetItem,
    QSplitter, QFrame, QGraphicsOpacityEffect, QScrollArea
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineSettings
from PyQt6.QtGui import (
    QIcon, QPixmap, QColor, QPalette, QFont, QFontDatabase,
    QAction, QKeySequence, QPainter, QLinearGradient, QBrush,
    QPen, QCursor, QShortcut
)

COLORS = {
    "bg":           "#0F1117",
    "surface":      "#1A1D27",
    "surface2":     "#22263A",
    "border":       "#2E3350",
    "accent":       "#5B8EF0",
    "accent_glow":  "#3D6FD4",
    "accent_soft":  "#1E2D5A",
    "text":         "#E8EAFF",
    "text_dim":     "#7B82A8",
    "text_muted":   "#4A5070",
    "success":      "#4ADE80",
    "warning":      "#FBBF24",
    "danger":       "#F87171",
    "tab_active":   "#1E2D5A",
    "tab_hover":    "#1A1D27",
}

STYLESHEET = f"""
/* ── Root ── */
QMainWindow, QWidget {{
    background-color: {COLORS['bg']};
    color: {COLORS['text']};
    font-family: 'Segoe UI', 'SF Pro Display', sans-serif;
    font-size: 13px;
    border: none;
}}

/* ── Tab Widget ── */
QTabWidget::pane {{
    border: none;
    background: {COLORS['bg']};
}}

QTabBar {{
    background: {COLORS['surface']};
}}

QTabBar::tab {{
    background: {COLORS['surface']};
    color: {COLORS['text_dim']};
    padding: 8px 14px 8px 12px;
    margin: 0px 1px 0px 0px;
    min-width: 140px;
    max-width: 240px;
    font-size: 12px;
    border-bottom: 2px solid transparent;
}}

QTabBar::tab:selected {{
    background: {COLORS['tab_active']};
    color: {COLORS['text']};
    border-bottom: 2px solid {COLORS['accent']};
}}

QTabBar::tab:hover:!selected {{
    background: {COLORS['surface2']};
    color: {COLORS['text']};
}}

QTabBar::tab:first {{
    border-top-left-radius: 0px;
}}

QTabBar::close-button {{
    image: none;
    subcontrol-position: right;
    padding: 2px;
}}

/* ── Toolbar ── */
QToolBar {{
    background: {COLORS['surface']};
    border-bottom: 1px solid {COLORS['border']};
    padding: 6px 10px;
    spacing: 6px;
}}

/* ── Nav Buttons ── */
QPushButton#navBtn {{
    background: transparent;
    border: none;
    border-radius: 8px;
    color: {COLORS['text_dim']};
    font-size: 16px;
    padding: 5px 9px;
    min-width: 32px;
    min-height: 32px;
}}

QPushButton#navBtn:hover {{
    background: {COLORS['surface2']};
    color: {COLORS['text']};
}}

QPushButton#navBtn:pressed {{
    background: {COLORS['border']};
}}

QPushButton#navBtn:disabled {{
    color: {COLORS['text_muted']};
}}

/* ── Accent Button ── */
QPushButton#accentBtn {{
    background: {COLORS['accent']};
    border: none;
    border-radius: 8px;
    color: white;
    font-size: 13px;
    font-weight: 600;
    padding: 6px 14px;
}}
QPushButton#accentBtn:hover {{
    background: {COLORS['accent_glow']};
}}

/* ── Address Bar ── */
QLineEdit#addressBar {{
    background: {COLORS['surface2']};
    border: 1.5px solid {COLORS['border']};
    border-radius: 10px;
    color: {COLORS['text']};
    font-size: 13px;
    padding: 6px 14px;
    selection-background-color: {COLORS['accent_soft']};
}}

QLineEdit#addressBar:focus {{
    border: 1.5px solid {COLORS['accent']};
    background: {COLORS['surface']};
}}

QLineEdit#addressBar:hover {{
    border: 1.5px solid {COLORS['accent_soft']};
}}

/* ── Progress Bar ── */
QProgressBar {{
    background: transparent;
    border: none;
    height: 2px;
    border-radius: 1px;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {COLORS['accent']}, stop:1 #A78BFA);
    border-radius: 1px;
}}

/* ── Status Bar ── */
QStatusBar {{
    background: {COLORS['surface']};
    border-top: 1px solid {COLORS['border']};
    color: {COLORS['text_muted']};
    font-size: 11px;
    padding: 2px 8px;
}}

/* ── Menu ── */
QMenu {{
    background: {COLORS['surface2']};
    border: 1px solid {COLORS['border']};
    border-radius: 10px;
    padding: 6px;
    color: {COLORS['text']};
}}
QMenu::item {{
    padding: 7px 20px;
    border-radius: 6px;
}}
QMenu::item:selected {{
    background: {COLORS['accent_soft']};
    color: {COLORS['accent']};
}}
QMenu::separator {{
    height: 1px;
    background: {COLORS['border']};
    margin: 4px 10px;
}}

/* ── Dialog ── */
QDialog {{
    background: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 14px;
}}

/* ── List Widget ── */
QListWidget {{
    background: {COLORS['surface2']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    color: {COLORS['text']};
    padding: 4px;
}}
QListWidget::item {{
    padding: 8px 12px;
    border-radius: 6px;
}}
QListWidget::item:selected {{
    background: {COLORS['accent_soft']};
    color: {COLORS['accent']};
}}
QListWidget::item:hover {{
    background: {COLORS['border']};
}}

/* ── Scroll Bar ── */
QScrollBar:vertical {{
    background: transparent;
    width: 6px;
    margin: 0;
}}
QScrollBar::handle:vertical {{
    background: {COLORS['border']};
    border-radius: 3px;
    min-height: 30px;
}}
QScrollBar::handle:vertical:hover {{
    background: {COLORS['text_muted']};
}}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0;
}}
QScrollBar:horizontal {{
    height: 6px;
    background: transparent;
}}
QScrollBar::handle:horizontal {{
    background: {COLORS['border']};
    border-radius: 3px;
}}

/* ── Label ── */
QLabel#sectionLabel {{
    color: {COLORS['text_muted']};
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 4px 4px 0px 4px;
}}

QLabel#titleLabel {{
    color: {COLORS['text']};
    font-size: 16px;
    font-weight: 700;
}}

/* ── Bookmark / History Panel ── */
QFrame#panel {{
    background: {COLORS['surface']};
    border-left: 1px solid {COLORS['border']};
}}

/* ── Security Badge ── */
QLabel#secureBadge {{
    color: {COLORS['success']};
    font-size: 11px;
    padding: 2px 6px;
    background: rgba(74, 222, 128, 0.1);
    border-radius: 5px;
}}
QLabel#insecureBadge {{
    color: {COLORS['warning']};
    font-size: 11px;
    padding: 2px 6px;
    background: rgba(251, 191, 36, 0.1);
    border-radius: 5px;
}}

/* ── New Tab Button ── */
QPushButton#newTabBtn {{
    background: transparent;
    border: 1px dashed {COLORS['border']};
    border-radius: 7px;
    color: {COLORS['text_dim']};
    font-size: 16px;
    min-width: 28px;
    min-height: 28px;
    max-width: 28px;
    max-height: 28px;
    padding: 0px;
}}
QPushButton#newTabBtn:hover {{
    background: {COLORS['surface2']};
    border-color: {COLORS['accent']};
    color: {COLORS['accent']};
}}

/* ── Home Page Search ── */
QLineEdit#homeSearch {{
    background: {COLORS['surface2']};
    border: 2px solid {COLORS['border']};
    border-radius: 14px;
    color: {COLORS['text']};
    font-size: 15px;
    padding: 12px 20px;
    min-width: 500px;
    selection-background-color: {COLORS['accent_soft']};
}}
QLineEdit#homeSearch:focus {{
    border: 2px solid {COLORS['accent']};
    background: {COLORS['surface']};
}}
"""

HOME_HTML = """
<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Нова вкладка</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #0F1117;
    color: #E8EAFF;
    font-family: 'Segoe UI', system-ui, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    overflow: hidden;
  }
  .bg-orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.12;
    pointer-events: none;
    animation: float 8s ease-in-out infinite;
  }
  .orb1 { width: 500px; height: 500px; background: #5B8EF0; top: -100px; right: -100px; }
  .orb2 { width: 400px; height: 400px; background: #A78BFA; bottom: -80px; left: -80px; animation-delay: -4s; }
  .orb3 { width: 300px; height: 300px; background: #34D399; top: 60%; left: 60%; animation-delay: -2s; }

  @keyframes float {
    0%, 100% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-20px) scale(1.03); }
  }

  .container { position: relative; z-index: 1; text-align: center; }

  .logo {
    font-size: 52px;
    font-weight: 800;
    letter-spacing: -2px;
    background: linear-gradient(135deg, #5B8EF0 0%, #A78BFA 50%, #34D399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
    animation: fadeUp 0.8s ease-out;
  }

  .tagline {
    color: #7B82A8;
    font-size: 14px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 48px;
    animation: fadeUp 0.8s ease-out 0.1s both;
  }

  .shortcuts {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 60px;
    animation: fadeUp 0.8s ease-out 0.2s both;
  }

  .shortcut {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 18px 14px;
    background: rgba(26, 29, 39, 0.8);
    border: 1px solid #2E3350;
    border-radius: 16px;
    cursor: pointer;
    text-decoration: none;
    color: #E8EAFF;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(10px);
    min-width: 90px;
  }

  .shortcut:hover {
    background: rgba(34, 38, 58, 0.9);
    border-color: #5B8EF0;
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(91, 142, 240, 0.15);
  }

  .shortcut .icon { font-size: 26px; }
  .shortcut .name { font-size: 11px; color: #7B82A8; }

  .time-widget {
    font-size: 64px;
    font-weight: 200;
    letter-spacing: -2px;
    color: #E8EAFF;
    margin-bottom: 6px;
    animation: fadeUp 1.3s ease-out 0.6s both;
    font-variant-numeric: tabular-nums;
  }
  .date-widget {
    color: #7B82A8;
    font-size: 13px;
    margin-bottom: 48px;
    animation: fadeUp 0.8s ease-out 0.35s both;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>
  <div class="bg-orb orb1"></div>
  <div class="bg-orb orb2"></div>
  <div class="bg-orb orb3"></div>

  <div class="container">
    <div class="time-widget" id="clock">00:00</div>
    <div class="date-widget" id="date"></div>
    <div class="logo">Домашня сторінка</div>

    <div class="shortcuts">
      <a class="shortcut" href="https://google.com">
        <div class="icon">🔍</div><div class="name">Google</div>
      </a>
      <a class="shortcut" href="https://youtube.com">
        <div class="icon">▶️</div><div class="name">YouTube</div>
      </a>
      <a class="shortcut" href="https://github.com">
        <div class="icon">🐙</div><div class="name">GitHub</div>
      </a>
      <a class="shortcut" href="https://wikipedia.org">
        <div class="icon">📚</div><div class="name">Wikipedia</div>
      </a>
      <a class="shortcut" href="https://twitter.com">
        <div class="icon">🐦</div><div class="name">Twitter</div>
      </a>
      <a class="shortcut" href="https://reddit.com">
        <div class="icon">🤖</div><div class="name">Reddit</div>
      </a>
      <a class="shortcut" href="https://translate.google.com">
        <div class="icon">🌐</div><div class="name">Перекладач</div>
      </a>
      <a class="shortcut" href="https://weather.com">
        <div class="icon">🌤️</div><div class="name">Погода</div>
      </a>
    </div>
  </div>

  <script>
    window.addEventListener("DOMContentLoaded", () => {
        updateClock();
        setInterval(updateClock, 1000);
    });

    function updateClock() {
      const now = new Date();
      const h = String(now.getHours()).padStart(2, '0');
      const m = String(now.getMinutes()).padStart(2, '0');
      document.getElementById('clock').textContent = h + ':' + m;

      const days = ['Неділя','Понеділок','Вівторок','Середа','Четвер',"П'ятниця",'Субота'];
      const months = ['січня','лютого','березня','квітня','травня','червня',
                      'липня','серпня','вересня','жовтня','листопада','грудня'];
      const d = days[now.getDay()];
      const dt = now.getDate();
      const mo = months[now.getMonth()];
      document.getElementById('date').textContent = `${d}, ${dt} ${mo} ${now.getFullYear()}`;
    }
    updateClock();
    setInterval(updateClock, 1000);
  </script>
</body>
</html>
"""

HOME_URL = "about:home"

class BrowserTab(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPage(QWebEnginePage(QWebEngineProfile.defaultProfile(), self))

    def createWindow(self, window_type):
        main = self.window()

        if hasattr(main, "add_tab"):
            return main.add_tab()

        return super().createWindow(window_type)


class ListDialog(QDialog):
    url_selected = pyqtSignal(str)

    def __init__(self, title: str, items: list[tuple[str, str]], parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setMinimumSize(480, 380)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        lbl = QLabel(title)
        lbl.setObjectName("titleLabel")

        layout.addWidget(lbl)

        self.list = QListWidget()

        layout.addWidget(self.list)

        for name, url in items:

            item = QListWidgetItem(f"  {name}")
            item.setData(Qt.ItemDataRole.UserRole, url)
            item.setToolTip(url)

            self.list.addItem(item)

        self.list.itemDoubleClicked.connect(self._on_select)

        btn_row = QHBoxLayout()
        btn_row.addStretch()

        close_btn = QPushButton("Закрити")
        close_btn.setObjectName("navBtn")
        close_btn.clicked.connect(self.reject)

        btn_row.addWidget(close_btn)

        layout.addLayout(btn_row)

    def _on_select(self, item):
        url = item.data(Qt.ItemDataRole.UserRole)
        self.url_selected.emit(url)
        self.accept()


class BrowserWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Браузер")
        self.setMinimumSize(1100, 720)
        self.resize(1360, 820)

        self._history: list[tuple[str, str]] = []
        self._bookmarks: list[tuple[str, str]] = []

        self._build_ui()
        self._build_shortcuts()
        self._add_new_tab(HOME_URL)

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # tab bar area
        tab_row = QHBoxLayout()
        tab_row.setContentsMargins(8, 6, 8, 0)
        tab_row.setSpacing(6)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self._close_tab)
        self.tabs.currentChanged.connect(self._on_tab_change)

        # new tab button
        new_tab_btn = QPushButton("+")
        new_tab_btn.setObjectName("newTabBtn")
        new_tab_btn.setToolTip("Нова вкладка (Ctrl+T)")
        new_tab_btn.clicked.connect(lambda: self._add_new_tab(HOME_URL))
        self.tabs.setCornerWidget(new_tab_btn, Qt.Corner.TopRightCorner)

        root.addWidget(self.tabs)

        # toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setIconSize(QSize(18, 18))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

        # nav buttons
        self.back_btn = self._nav_btn("◀", "Назад (Alt+←)", self._go_back)
        self.fwd_btn  = self._nav_btn("▶", "Вперед (Alt+→)", self._go_forward)
        self.reload_btn = self._nav_btn("↻", "Оновити (F5)", self._reload)
        self.home_btn = self._nav_btn("⌂", "Домашня (Alt+Home)", self._go_home)

        for btn in [self.back_btn, self.fwd_btn, self.reload_btn, self.home_btn]:
            toolbar.addWidget(btn)

        toolbar.addSeparator()

        # security badge
        self.sec_badge = QLabel("🔒")
        self.sec_badge.setObjectName("secureBadge")
        self.sec_badge.setFixedWidth(30)
        toolbar.addWidget(self.sec_badge)

        # address bar
        self.address_bar = QLineEdit()
        self.address_bar.setObjectName("addressBar")
        self.address_bar.setPlaceholderText("Введіть адресу або пошуковий запит…")
        self.address_bar.returnPressed.connect(self._navigate)
        self.address_bar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        toolbar.addWidget(self.address_bar)

        # bookmark button
        self.bm_btn = self._nav_btn("☆", "Додати до закладок", self._toggle_bookmark)
        toolbar.addWidget(self.bm_btn)

        toolbar.addSeparator()

        # menu button
        menu_btn = self._nav_btn("⋮", "Меню", None)
        menu_btn.setMenu(self._build_menu())
        toolbar.addWidget(menu_btn)

        # progress bar (thin, under toolbar)
        self.progress = QProgressBar()
        self.progress.setMaximumHeight(3)
        self.progress.setTextVisible(False)
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.hide()
        self.addToolBarBreak()

        prog_toolbar = QToolBar()
        prog_toolbar.setMovable(False)
        prog_toolbar.setFloatable(False)
        prog_toolbar.setMaximumHeight(3)
        prog_toolbar.setContentsMargins(0, 0, 0, 0)
        prog_widget = QWidget()
        prog_layout = QHBoxLayout(prog_widget)
        prog_layout.setContentsMargins(0, 0, 0, 0)
        prog_layout.addWidget(self.progress)
        prog_toolbar.addWidget(prog_widget)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, prog_toolbar)

        # status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Готово")

    def _nav_btn(self, text, tip, callback):
        btn = QPushButton(text)

        btn.setObjectName("navBtn")
        btn.setToolTip(tip)
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        if callback:
            btn.clicked.connect(callback)

        return btn

    def _build_menu(self):
        # menu
        m = QMenu(self)
        m.addAction("🔖  Закладки", self._show_bookmarks)
        m.addAction("📜  Історія", self._show_history)
        m.addSeparator()
        m.addAction("🔍  Знайти на сторінці", self._find_on_page)
        m.addAction("🔄  Перезавантажити", self._reload)
        m.addSeparator()
        m.addAction("❌  Вийти", self.close)
        return m

    def _build_shortcuts(self):
        """
        Shortcuts for the browser
            Ctrl+t: New tab/Нова вкладка
            Ctrl+W: Close tab/Закрити вкладку
            Ctrl+L: Focus on adress bar/Фокус на адресну строку
            F5: Reload page/Перезавантажити сторінку
            Alt+Left: Back/Повернутись
            Alt+Right: Forward/Вперед
            Alt+Home: Home/Домашня сторінка
            Ctrl+D: Toggle bookmarks/Закладка
            Ctrl+H: History/Історія
            Ctrl+B: Show bookmarks/Показати Закладки
            Ctrl+F: Find in page/Пошук у сторінці
        """
        QShortcut(QKeySequence("Ctrl+T"), self, lambda: self._add_new_tab(HOME_URL))
        QShortcut(QKeySequence("Ctrl+W"), self, self._close_current_tab)
        QShortcut(QKeySequence("Ctrl+L"), self, lambda: (self.address_bar.selectAll(), self.address_bar.setFocus()))
        QShortcut(QKeySequence("F5"),      self, self._reload)
        QShortcut(QKeySequence("Alt+Left"),  self, self._go_back)
        QShortcut(QKeySequence("Alt+Right"), self, self._go_forward)
        QShortcut(QKeySequence("Alt+Home"),  self, self._go_home)
        QShortcut(QKeySequence("Ctrl+D"),    self, self._toggle_bookmark)
        QShortcut(QKeySequence("Ctrl+H"),    self, self._show_history)
        QShortcut(QKeySequence("Ctrl+B"),    self, self._show_bookmarks)
        QShortcut(QKeySequence("Ctrl+F"),    self, self._find_on_page)

    def _add_new_tab(self, url: str = HOME_URL) -> BrowserTab:
        """
        Creates new tab

            Creates new tab in self.tabs
            switches to it
            reconnects all parts to it        
        """
        view = BrowserTab(self)

        idx = self.tabs.addTab(view, "Нова вкладка")
        self.tabs.setCurrentIndex(idx)

        view.titleChanged.connect(lambda t, v=view: self._update_tab_title(v, t))
        view.urlChanged.connect(lambda u, v=view: self._on_url_change(u, v))
        view.loadStarted.connect(self._on_load_start)
        view.loadProgress.connect(self._on_load_progress)
        view.loadFinished.connect(self._on_load_finish)
        view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptEnabled,
            True
        )

        self._load_url(view, url)
        return view

    def add_tab(self) -> BrowserTab:
        """Adds new tab with no url"""
        return self._add_new_tab(HOME_URL)

    def _close_tab(self, idx):
        """Closes tab (1 tab = go home)"""
        if self.tabs.count() <= 1:
            self._add_new_tab(HOME_URL)

        self.tabs.removeTab(idx)

    def _close_current_tab(self):
        """Close current tab"""
        self._close_tab(self.tabs.currentIndex())

    def _current_view(self) -> BrowserTab | None:
        """Returns current BrowserTab (focused)"""
        w = self.tabs.currentWidget()
        return w if isinstance(w, BrowserTab) else None

    def _on_tab_change(self, idx):
        v = self._current_view()
        if v:
            url = v.url().toString()
            self.address_bar.setText("" if url == HOME_URL else url)
            self._update_security(url)

    def _update_tab_title(self, view: BrowserTab, title: str):
        """Updates tab title (if no title -> Нова вкладка)"""
        i = self.tabs.indexOf(view)

        if i >= 0:
            short = (title[:22] + "…") if len(title) > 25 else title
            self.tabs.setTabText(i, short or "Нова вкладка")
            self.tabs.setTabToolTip(i, title)

    def _load_url(self, view: BrowserTab, url: str):
        """Loads url"""
        if url == HOME_URL:
            view.setHtml(HOME_HTML, QUrl("about:home"))
        else:
            view.load(QUrl(url))

    def _navigate(self):
        """
        Navigate to url
            if not http/s, file/about: -> google search
        """
        raw = self.address_bar.text().strip()

        if not raw:
            return

        v = self._current_view()

        if not v:
            return

        if raw.startswith(("http://", "https://", "file://", "about:")):
            url = raw

        elif "." in raw and " " not in raw:
            url = "https://" + raw

        else:
            url = "https://www.google.com/search?q=" + raw.replace(" ", "+")


        self._load_url(v, url)

    def _go_back(self):
        """Go back to previous view (using history)"""
        v = self._current_view()
        if v and v.history().canGoBack():
            v.back()

    def _go_forward(self):
        """Go forward to next view (using history)"""
        v = self._current_view()
        if v and v.history().canGoForward():
            v.forward()

    def _reload(self):
        """Reload the page"""
        v = self._current_view()
        if v:
            v.reload()

    def _go_home(self):
        """Go home"""
        v = self._current_view()
        if v:
            self._load_url(v, HOME_URL)

    def _on_url_change(self, url: QUrl, view: BrowserTab):
        """Manage url change"""
        if self._current_view() is view:
            s = url.toString()
            self.address_bar.setText("" if s in ("about:home", "about:blank") else s)
            self._update_security(s)
            self.back_btn.setEnabled(view.history().canGoBack())
            self.fwd_btn.setEnabled(view.history().canGoForward())

        title = view.title() or url.host()
        s = url.toString()

        if s and s not in ("about:home", "about:blank"):
            self._history = [(t, u) for t, u in self._history if u != s]
            self._history.insert(0, (title or s, s))
            self._history = self._history[:200]

    def _on_load_start(self):
        """On load start (if page have not loaded yet, can be canceled)"""
        self.progress.setValue(0)
        self.progress.show()

        v = self._current_view()

        if v:
            self.reload_btn.setText("✕")
            self.reload_btn.setToolTip("Зупинити")
            self.reload_btn.clicked.disconnect()
            self.reload_btn.clicked.connect(v.stop)

    def _on_load_progress(self, p):
        """On load progress"""
        self.progress.setValue(p)

    def _on_load_finish(self, ok):
        """On load finish"""
        self.progress.setValue(100)
        QTimer.singleShot(500, self.progress.hide)
        self.reload_btn.setText("↻")
        self.reload_btn.setToolTip("Оновити (F5)")

        try:
            self.reload_btn.clicked.disconnect()

        except TypeError:
            pass

        self.reload_btn.clicked.connect(self._reload)
        v = self._current_view()

        if v:
            self.status.showMessage(v.url().toString() if ok else "Помилка завантаження", 3000)

    def _update_security(self, url: str):
        """Update security icon"""

        if url.startswith("https://"):
            self.sec_badge.setText("🔒")
            self.sec_badge.setObjectName("secureBadge")

        elif url.startswith("http://"):
            self.sec_badge.setText("⚠️")
            self.sec_badge.setObjectName("insecureBadge")

        else:
            self.sec_badge.setText("  ")

        self.sec_badge.setStyleSheet("") # force refresh

    def _toggle_bookmark(self):
        """Add to bookmarks"""
        v = self._current_view()
        if not v:
            return

        url = v.url().toString()
        title = v.title() or url

        if url in ("about:home", "about:blank", ""):
            return

        existing = [u for _, u in self._bookmarks]

        if url in existing:
            self._bookmarks = [(t, u) for t, u in self._bookmarks if u != url]
            self.bm_btn.setText("☆")
            self.status.showMessage("Закладку видалено", 2000)

        else:
            self._bookmarks.insert(0, (title, url))
            self.bm_btn.setText("★")
            self.status.showMessage("Сторінку збережено до закладок", 2000)

    def _show_bookmarks(self):
        """Show bookmarks (via ListDialog)"""
        if not self._bookmarks:
            self.status.showMessage("Закладок немає", 2000)
            return

        dlg = ListDialog("Закладки", self._bookmarks, self)
        dlg.url_selected.connect(lambda u: self._load_url(self._current_view(), u))
        dlg.exec()

    def _show_history(self):
        """Show history (via ListDialog)"""
        if not self._history:
            self.status.showMessage("Історія порожня", 2000)
            return

        dlg = ListDialog("Історія", self._history, self)
        dlg.url_selected.connect(lambda u: self._load_url(self._current_view(), u))
        dlg.exec()

    def _find_on_page(self):
        """Find on page"""
        self.status.showMessage("Ctrl+F — пошук через адресний рядок браузера", 3000)


def main():
    # HiDPI support
    os.environ.setdefault("QT_ENABLE_HIGHDPI_SCALING", "1")

    app = QApplication(sys.argv)
    app.setApplicationName("Браузер")
    app.setOrganizationName("LocalBrowser")

    # apply css/html
    app.setStyleSheet(STYLESHEET)

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window,          QColor(COLORS["bg"]))
    palette.setColor(QPalette.ColorRole.WindowText,      QColor(COLORS["text"]))
    palette.setColor(QPalette.ColorRole.Base,            QColor(COLORS["surface2"]))
    palette.setColor(QPalette.ColorRole.AlternateBase,   QColor(COLORS["surface"]))
    palette.setColor(QPalette.ColorRole.Text,            QColor(COLORS["text"]))
    palette.setColor(QPalette.ColorRole.Button,          QColor(COLORS["surface"]))
    palette.setColor(QPalette.ColorRole.ButtonText,      QColor(COLORS["text"]))
    palette.setColor(QPalette.ColorRole.Highlight,       QColor(COLORS["accent"]))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Link,            QColor(COLORS["accent"]))
    app.setPalette(palette)

    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
