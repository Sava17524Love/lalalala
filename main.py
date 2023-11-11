from PyQt5.QtWidgets import (QAppLication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout )

app = QAppLication([])

notes_win = QWidget()
notes_win.setWindowTitle('')
notes_win.resize(900, 600)
list_notes = QListWidget()
list_notes_label = QLabel('')
button_note_del = QPushButton('')
button_note_create = QPushButton('')
button_note_save = QPushButton('')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('')
field_text = QTextEdit()
button_note_add = QPushButton('')
button_note_del = QPushButton('')
button_note_search = QPushButton('')
list_tags = QListWidget()
list_tags_label = QLabel()

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(list_notes)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_note_add)
row_3.addWidget(button_note_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_note_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)
notes_win.show()
app.exec_()
