import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRegExp,QSize

textchanged=False
url=""
class my_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gelişmiş Text Editör")
        self.setWindowIcon(QIcon("notepad.png"))
        self.setGeometry(450,150,1000,800)
        self.UI()
    
    def UI(self):
        self.editor=QTextEdit(self)
        self.setCentralWidget(self.editor)# ---> TextEdit'i pencerenin merkezine alır ve onla birlikte hareket ettirir.
        self.editor.setFontPointSize(12.0)# ---> Standart pointsize'i ayarlar.
        self.menu()
        self.toolbar()
        self.dockbar()
        
        self.editor.textChanged.connect(self.textchanged)
        self.statusbar()
    
    def menu(self):
    #########################################################################################       ANA MENÜ :
        menu=self.menuBar()#---> ana menü böyle oluşturulur, ana menüye bir şeyler eklemek istersek de -> menu.addMenu("") 
        dosya=menu.addMenu("Dosyalar")
        edit=menu.addMenu("Düzenle")
        view=menu.addMenu("Görüntüle")
        help=menu.addMenu("Yardım")
        
        
    #########################################################################################       DOSYA ALT MENÜ :
        new = QAction(QIcon("new.png"),"Yeni",self)
        new.setShortcut("Ctrl+N")
        new.triggered.connect(self.newf)
        dosya.addAction(new)
        
        open=QAction(QIcon("open.png"),"Aç",self)
        open.setShortcut("Ctrl+O")
        open.triggered.connect(self.openf)
        dosya.addAction(open)
        
        save=QAction(QIcon("save.png"),"Kaydet",self)
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.savef)
        dosya.addAction(save)
        
        eksit=QAction(QIcon("exit.png"),"Çıkış",self)
        eksit.triggered.connect(self.eksitf)
        dosya.addAction(eksit)
        

    #########################################################################################       EDİT ALT MENÜ :
        undo=QAction(QIcon("undo.png"),"Geri Al",self)
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.undof)
        edit.addAction(undo)
        
        cut=QAction(QIcon("cut.png"),"Kes",self)
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.cutf)
        edit.addAction(cut)
        
        copy=QAction(QIcon("copy.png"),"Kopyala",self)
        copy.setShortcut("Ctrl+C")
        copy.triggered.connect(self.copyf)
        edit.addAction(copy)
        
        paste=QAction(QIcon("paste.png"),"Yapıştır",self)
        paste.setShortcut("Ctrl+V")
        paste.triggered.connect(self.pastef)
        edit.addAction(paste)
        
        find=QAction(QIcon("find.png"),"Bul",self)
        find.setShortcut("Ctrl+F")
        find.triggered.connect(self.findf)
        edit.addAction(find)
        
        time_date=QAction(QIcon("datetime.png"),"Zaman Ekle",self)
        time_date.triggered.connect(self.timef)
        time_date.setShortcut("F5")
        edit.addAction(time_date)
        
        
    #########################################################################################       VİEW ALT MENÜ :
        tooglestatusbar=QAction("StatusBar",self,checkable=True)
        tooglestatusbar.triggered.connect(self.sbf)
        view.addAction(tooglestatusbar)
        
        toogletoolbar=QAction("ToolBar",self,checkable=True)
        toogletoolbar.triggered.connect(self.tbf)
        view.addAction(toogletoolbar)
        
        toogledockbar=QAction("DockBar",self,checkable=True)
        toogledockbar.triggered.connect(self.dbf)
        view.addAction(toogledockbar)
        

    #########################################################################################       HELP ALT MENÜ :
        about_us=QAction("Hakkında",self)
        about_us.setIcon(QIcon("about.png"))
        about_us.triggered.connect(self.auf)
        help.addAction(about_us)

        
    #########################################################################################       FONKSİYONLAR :

    def newf(self):
        pass

    def openf(self):
        pass
    
    def savef(self):
        pass
    
    def eksitf(self):
       pass
    
    
    def undof(self):
        pass
    def cutf(self):
        pass
    def copyf(self):
        pass
    def pastef(self):
        pass
    def findf(self):
        pass
    def timef(self):
        pass

    
    
    def sbf(self):
        pass
    def tbf(self):
        pass
    def dbf(self):
        pass


    def auf(self):
        pass

    
    #########################################################################################       TOOL BAR :
    def toolbar(self):
        self.tb=self.addToolBar("Tool Bar")
        self.fontfamily=QFontComboBox(self)
        self.tb.addWidget(self.fontfamily)
        self.tb.addSeparator()
        self.tb.addSeparator()
        
        
        self.fontsize=QComboBox(self)
        self.tb.addWidget(self.fontsize)
        for i in range(8,65,2):
            self.fontsize.addItem(str(i))
        self.fontsize.setCurrentText("14")
        self.tb.addSeparator()
        self.tb.addSeparator()
        
        self.bold=QAction(QIcon("bold.png"),"Bold Uygula",self)
        self.tb.addAction(self.bold)#QAction olarak atadığımız içine addAction olarak eklemeliyiz.
        
        self.italic=QAction(QIcon("italic.png"),"İtalic Uygula",self)
        self.tb.addAction(self.italic)
    
        self.underline=QAction(QIcon("underline.png"),"Altını Çiz",self)
        self.tb.addAction(self.underline)
        
        self.tb.addSeparator()
        self.tb.addSeparator()
        
        
        self.fontcolor=QAction(QIcon("color.png"),"Renk Değiştir",self)
        self.tb.addAction(self.fontcolor)
        
        self.backcolor=QAction(QIcon("backcolor.png"),"Arka Rengi Değiştir",self)    
        self.tb.addAction(self.backcolor)
        
        self.alignleft=QAction(QIcon("alignleft.png"),"Sola Hizala",self)
        self.tb.addAction(self.alignleft)

        self.aligncenter=QAction(QIcon("aligncenter.png"),"Ortaya Hizala",self)
        self.tb.addAction(self.aligncenter)
        
        self.alignright=QAction(QIcon("alignright.png"),"Sağa Hizala",self)
        self.tb.addAction(self.alignright)
        
        self.alignjustify=QAction(QIcon("alignjustify.png"),"Yasla",self)
        self.tb.addAction(self.alignjustify)
        
        self.tb.addSeparator()
        self.tb.addSeparator()
        
        
        self.bulletlist=QAction(QIcon("bulletlist.png"),"Listele",self)
        self.tb.addAction(self.bulletlist)
        
        self.numberedlist=QAction(QIcon("numberlist.png"),"Numara ile Listele",self)
        self.tb.addAction(self.numberedlist)

    
    #########################################################################################       DOCK BAR :

    def dockbar(self):
        self.dock=QDockWidget("Dock",self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock)
        self.dockWidget=QWidget(self)
        self.dock.setWidget(self.dockWidget)
        formlayout=QFormLayout()
        
        findb=QToolButton()
        findb.setIcon(QIcon("find_large.png"))
        findb.setText("Ara")
        findb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        findb.setIconSize(QSize(50,50))
        findb.setCheckable(True)
        
        newb=QToolButton()
        newb.setIcon(QIcon("new_large.png"))
        newb.setIconSize(QSize(50,50))
        newb.setText("Yeni")
        newb.setCheckable(True)
        newb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        saveb=QToolButton()
        saveb.setIcon(QIcon("save_large.png"))
        saveb.setIconSize(QSize(50,50))
        saveb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        saveb.setText("Kaydet")
        saveb.setCheckable(True)
        
        openb=QToolButton()
        openb.setIcon(QIcon("open_large.png"))
        openb.setIconSize(QSize(50,50))
        openb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        openb.setCheckable(True)
        openb.setText("Aç")
        
        formlayout.addRow(newb,openb)
        formlayout.addRow(saveb,findb)
        self.dockWidget.setLayout(formlayout)
        
        self.tb.addSeparator()
        self.tb.addSeparator()
        
        
    #########################################################################################       STATUS BAR :
    def statusbar(self):
        self.status_bar=QStatusBar()
        self.setStatusBar(self.status_bar)
        
    def textchanged(self):
        global textchanged
        textchanged = True
        
        text=self.editor.toPlainText()
        harf=len(text)
        kelime=len(text.split())
        self.status_bar.showMessage(f"kelime sayısı -> {kelime}\tharf sayısı -> {harf}")

def window():
    
    app = QApplication(sys.argv)
    win = my_window()# win değişkenini yarattığımız class'tan bir nesne gibi yaptık

    win.show()
    sys.exit(app.exec_())

window()
