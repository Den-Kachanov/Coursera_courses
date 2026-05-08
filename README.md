# Python GUI Development with PyQt — Coursera

This repository contains all code written during the **Python GUI Development with PyQt** specialization on Coursera (Beginner and Intermediate levels). The course material was based on PyQt5, however all code in this repository was written using **PyQt6** — the newer and more up-to-date version of the framework. The majority of the API between the two versions is identical, with minor differences in import namespaces and flag handling.

---

## Repository Structure

```
Coursera_courses/
├── course 1/
│   ├── module 1/          # Core widgets and basic application structure
│   └── module 2/          # Layouts, menus, toolbars, signals and dialogs
├── course 2/
│   ├── module 1/          # Drawing, clipboard and message dialogs
│   └── module 2/          # Pen & brush styles, drag & drop, image display
└── project/               # Independent project: web browser built with PyQt6
```

---

## Course 1 — Beginner Level

### Module 1 — Widgets and Application Basics

| File | Description |
|------|-------------|
| `FirstApp.py` | A minimal PyQt6 application. Creates and displays a blank `QWidget` window — the entry point for understanding the application lifecycle (`QApplication`, `exec()`). |
| `LabelDemo.py` | Demonstrates the use of `QLabel` to display static text inside a window. |
| `TextBoxDemo.py` | Implements a text input field using `QLineEdit` alongside a `QPushButton`. Demonstrates basic signal-slot connection: the button click triggers reading and printing the input value. |
| `RadioButtonDemo.py` | Creates a group of `QRadioButton` widgets arranged with `QGridLayout`. Uses the `toggled` signal and a custom attribute on each button to identify the selected option. |
| `CheckBoxDemo.py` | Builds a checkbox list using `QCheckBox` to represent multiple-choice input (hobbies). Demonstrates default checked state via `toggle()`. |
| `ComboBoxDemo.py` | Implements a dropdown menu with `QComboBox`. Connects the `textActivated` signal to a handler that dynamically updates a `QLabel` with the selected value. |

### Module 2 — Layouts, Controls and Events

| File | Description |
|------|-------------|
| `SliderDemo.py` | Creates a horizontal `QSlider` with tick marks and range configuration. Connects `valueChanged` signal to a `QLabel` to display the current value in real time. |
| `MenuBarDemo.py` | Builds a `QMainWindow` with a multi-item `QMenuBar` (File, Edit, Font, View) and a `QStatusBar`. Implements a checkable `QAction` in the View menu to toggle visibility of the status bar. |
| `DialogBoxDemo.py` | Demonstrates input dialogs using `QInputDialog.getText()`. The entered text is written back into a `QLineEdit` field. |
| `ToolBarDemo.py` | Adds a `QToolBar` to `QMainWindow` containing an exit action with a custom icon (`QIcon`) and keyboard shortcut (`Ctrl+E`). |
| `SignalDemo.py` | Illustrates the Qt signal-slot mechanism by connecting a `QSlider`'s `valueChanged` signal directly to a `QLCDNumber`'s `display` slot, with no intermediate handler. |

---

## Course 2 — Intermediate Level

### Module 1 — Drawing and System Dialogs

| File | Description |
|------|-------------|
| `CircleDrawDemo.py` | Draws a full-size ellipse using `QPainter`, `QPen` (dashed red border, width 5), and `QBrush` (yellow cross-hatch fill) inside the `paintEvent` handler. |
| `RectangleDrawDemo.py` | Draws a styled rectangle using the same `QPainter` approach with `DashLine` pen and `CrossPattern` brush. |
| `TriangleDrawDemo.py` | Constructs a triangle using `QPainterPath` with sequential `lineTo()` calls. Demonstrates path-based drawing as an alternative to primitive shape methods. |
| `ArrowDemo.py` | Draws a basic arrow shape using three `drawLine()` calls with antialiasing enabled via `QPainter.RenderHint.Antialiasing`. |
| `ClipBoardDemo.py` | Implements clipboard monitoring using `QApplication.clipboard()`. Connects the `dataChanged` signal to automatically append any new clipboard text into a `QPlainTextEdit` field. |
| `MessageBoxDemo.py` | Shows a `QMessageBox.warning()` dialog with Yes/No buttons on startup, and exits the application conditionally based on the user's choice. |

### Module 2 — Advanced Painting, Drag & Drop and Images

| File | Description |
|------|-------------|
| `Pen_BrushDemo.py` | Demonstrates six different `QPen` line styles: `SolidLine`, `DashLine`, `DashDotLine`, `DotLine`, `DashDotDotLine`, and a custom dash pattern defined via `setDashPattern()`. |
| `BrushDemo.py` | Renders a grid of rectangles each filled with a different `QBrush` pattern style, including `SolidPattern`, `Dense1–6Pattern`, `DiagCrossPattern`, `HorPattern`, `VerPattern`, and `BDiagPattern`. |
| `Drag_DropDemo.py` | Implements drag-and-drop functionality by subclassing `QPushButton` into `DragButton`, overriding `dragEnterEvent` and `dropEvent`, and enabling drag on a `QLineEdit` source. |
| `ImageDispDemo.py` | Loads and displays an image using `QPixmap` with aspect-ratio-preserving scaling (`KeepAspectRatio`). The image is embedded in a `QLabel` placed inside a `QGridLayout`. |

---

## Independent Project — PyQt6 Web Browser

As a capstone project, a fully functional desktop **web browser** was developed using PyQt6 and `PyQt6-WebEngine`. The application is structured around three custom classes and a complete dark-themed UI defined entirely through a QSS stylesheet and `QPalette`.

Source code is located in the [`project/`](./project) directory.

### Architecture

The project is composed of three classes:

**`BrowserTab(QWebEngineView)`** — A subclass of `QWebEngineView` that represents a single browser tab. Overrides `createWindow()` to intercept link-triggered window requests and redirect them into new tabs within the same application instead of spawning a separate window.

**`ListDialog(QDialog)`** — A reusable modal dialog built around `QListWidget`. Accepts a list of `(title, url)` tuples and displays them as selectable items. Emits a custom `pyqtSignal` (`url_selected`) on double-click, which is connected externally to the navigation logic. Used for both the bookmarks panel and the browsing history panel.

**`BrowserWindow(QMainWindow)`** — The main application window. Manages all UI construction, tab lifecycle, navigation state, and user interactions.

### Features

**Tabbed browsing.** Implemented with `QTabWidget` in document mode, with closable and reorderable tabs. Tab titles are truncated to 25 characters with an ellipsis. A "+" button is placed in the top-right corner of the tab bar via `setCornerWidget()` to open new tabs.

**Navigation toolbar.** Contains Back, Forward, Reload/Stop, and Home buttons built with a shared `_nav_btn()` factory method. The Reload button dynamically switches to a Stop ("✕") action during page loading by disconnecting and reconnecting its `clicked` signal, then reverts to "↻" on load completion.

**Smart address bar.** The `_navigate()` method applies three-branch URL resolution: if the input begins with `http://`, `https://`, `file://`, or `about:` it is used as-is; if it contains a dot and no spaces, `https://` is prepended automatically; otherwise the input is forwarded to a Google search query.

**Security indicator.** A `QLabel` badge to the left of the address bar updates on every URL change: it displays a green locked badge for HTTPS connections and a yellow warning badge for plain HTTP.

**Load progress bar.** A 3px-tall `QProgressBar` is embedded in a second `QToolBar` directly below the main toolbar. It is hidden by default, shown on `loadStarted`, updated on `loadProgress`, and hidden 500ms after `loadFinished` using `QTimer.singleShot()`.

**Bookmarks.** The bookmark button (☆/★) in the toolbar calls `_toggle_bookmark()`, which adds or removes the current page from an in-memory list of `(title, url)` tuples. The button icon updates to reflect the current bookmark state. Bookmarks are displayed in a `ListDialog`.

**Browsing history.** Every URL change appends a `(title, url)` entry to an in-memory list, capped at 200 entries. Duplicate URLs are removed before insertion to keep the list deduplicated. History is displayed in a `ListDialog`.

**Dropdown menu.** A `QMenu` attached to the "⋮" toolbar button provides access to bookmarks, history, find on page, reload, and exit actions.

**Keyboard shortcuts.** Registered via `QShortcut`:

| Shortcut | Action |
|----------|--------|
| `Ctrl+T` | New tab |
| `Ctrl+W` | Close current tab |
| `Ctrl+L` | Focus address bar and select all |
| `F5` | Reload page |
| `Alt+Left` | Navigate back |
| `Alt+Right` | Navigate forward |
| `Alt+Home` | Go to home page |
| `Ctrl+D` | Toggle bookmark |
| `Ctrl+H` | Show history |
| `Ctrl+B` | Show bookmarks |
| `Ctrl+F` | Find on page |

**Custom home page.** The `about:home` page is rendered from an embedded HTML string (`HOME_HTML`) via `QWebEngineView.setHtml()`. It features a dark background with three animated gradient blur orbs, a live digital clock and date display in Ukrainian (updated every second via JavaScript's `setInterval`), a gradient logo, and a grid of eight website shortcut tiles (Google, YouTube, GitHub, Wikipedia, Twitter, Reddit, Google Translate, Weather).

**Theming.** A 16-color palette is defined in the `COLORS` dictionary and injected into a complete QSS stylesheet covering all widget types used in the application: `QMainWindow`, `QTabBar`, `QToolBar`, `QPushButton`, `QLineEdit`, `QProgressBar`, `QStatusBar`, `QMenu`, `QDialog`, `QListWidget`, and `QScrollBar`. The application-level `QPalette` is also configured programmatically to match the dark theme across all system-rendered elements.

**HiDPI support.** The `QT_ENABLE_HIGHDPI_SCALING` environment variable is set before application startup to enable proper scaling on high-resolution displays.

### Requirements

```bash
pip install PyQt6 PyQt6-WebEngine
```

---

## Technologies

- **Language:** Python 3
- **GUI Framework:** PyQt6, PyQt6-WebEngine
- **Course Platform:** Coursera — Python GUI Development with PyQt (Beginner + Intermediate)

---

## Course Requirements

```bash
pip install PyQt6
```

---

## Author

**Denys Kachanov**  
GitHub: [Den-Kachanov](https://github.com/Den-Kachanov)
