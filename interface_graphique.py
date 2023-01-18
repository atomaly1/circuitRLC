import sys

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QAction, QBrush, QPen, QFont, QColor
from PySide6.QtWidgets import QWidget, QLabel, QApplication, QFrame, QGraphicsScene, QGraphicsView, QGraphicsItem




class FrameWithBorder(QFrame):
    DEFAULT_BORDURE = True

    def __init__(self):
        super().__init__()

    # DEFAULT_BORDURE peut être utilisé dans __init__
    def __init__(self,bordure : bool = DEFAULT_BORDURE):
        super().__init__()
        if bordure :
            self.setFrameStyle(QFrame.Panel | QFrame.Plain)
            self.setLineWidth(0)

            

class InterfaceGraphique(FrameWithBorder):

    def __init__(self):
        super().__init__()

        #self.draw_axis()
        #self.create_ui()
        self.show()

    def enterEvent(self, event):
        self.setCursor(Qt.CrossCursor)
    '''
    def mouseMoveEvent(self, event):
        self.update_points()
        self.points.append(event.pos())
        pos = event.pos()
        self.parent().statusBar().showMessage("x: {}, y: {}".format(pos.x(), pos.y()))
    #def mousePressEvent(self, event):
        #if event.button() == Qt.LeftButton:
            #self.points.append(event.pos())
    '''
    
    def draw_axis(self):
        
        scene = QGraphicsScene(self)
        
        # Définition des pinceaux
        redPen = QPen(Qt.red)
        redPen.setWidth(1)

        max_size_x = 2560/2                #FHD = 1920 ; QHD = 2560
        max_size_y = 1440/2               #FHD = 1080 ; QHD = 1440

        min_x = -(max_size_x)/2
        max_x = (max_size_x)/2

        min_y = -(max_size_y)/2
        max_y = (max_size_y)/2

        # axes
        axe_x = scene.addLine(min_x, 0, max_x, 0, redPen)          #axe abscisses
        axe_y = scene.addLine(0, min_y, 0, max_y, redPen)          #axe ordonnées

        taille_indentation = 10

        x = min_x
        text_x0 = scene.addText("-x", QFont("Sanserif", 15))
        text_x0.setPos(QPointF(x, 0))
        while x <= max_x:
            scene.addLine(x, -(taille_indentation/2), x, (taille_indentation/2), redPen)
            x = x + 10
        text_x1 = scene.addText("x", QFont("Sanserif", 15))
        text_x1.setPos(QPointF(x, 0))

        y = min_y
        text_y0 = scene.addText("-y", QFont("Sanserif", 15))
        text_y0.setPos(QPointF(0, y))
        while y <= max_y:
            scene.addLine(-(taille_indentation/2), y, (taille_indentation/2), y, redPen)
            y = y + 10
        
        text_y1 = scene.addText("+y", QFont("Sanserif", 15))
        text_y1.setPos(QPointF(0, y))

        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(0, 0, max_size_x, max_size_y)

    def create_ui(self):

        scene = QGraphicsScene(self)
 
        # Définition des pinceaux 
        blackPen = QPen(Qt.black)
        blackPen.setWidth(2)

        #def create_resistance(self, px, py, name):
        self.rect = scene.addRect(0, -100, 1,1, blackPen)
        #self.rect.setFlag(QGraphicsItem.ItemIsMovable)

        max_size_x = 2560/2                #FHD = 1920 ; QHD = 2560
        max_size_y = 1440/2               #FHD = 1080 ; QHD = 1440

        min_x = -(max_size_x)/2
        max_x = (max_size_x)/2

        min_y = -(max_size_y)/2
        max_y = (max_size_y)/2

        #test circuit test

        #noeuds #TODO : remplacer par classes et methodes

        n_diameter = 20
        n_radius = n_diameter/2

            #noeud 1
        n1_x = min_x/2
        n1_y = -min_y/2
        n1 = scene.addEllipse(n1_x-n_radius, n1_y-n_radius, n_diameter, n_diameter, blackPen)
        n1_text = scene.addText("N1", QFont("Sanserif", 15))
        n1_text.setPos(QPointF(n1_x, n1_y))

            #noeud 2
        n2_x = min_x/2
        n2_y = min_y/2
        n2 = scene.addEllipse(n2_x-n_radius, n2_y-n_radius, n_diameter, n_diameter, blackPen)
        n1_text = scene.addText("N2", QFont("Sanserif", 15))
        n1_text.setPos(QPointF(n2_x, n2_y))

            #noeud 3
        n3_x = -min_x/2
        n3_y = min_y/2
        n3 = scene.addEllipse(n3_x-n_radius, n3_y-n_radius, n_diameter, n_diameter, blackPen)
        n1_text = scene.addText("N3", QFont("Sanserif", 15))
        n1_text.setPos(QPointF(n3_x, n3_y))


            #noeud 4
        n4_x = -min_x/2
        n4_y = -min_y/2
        n4 = scene.addEllipse(n4_x-n_radius, n4_y-n_radius, n_diameter, n_diameter, blackPen)
        n1_text = scene.addText("N4", QFont("Sanserif", 15))
        n1_text.setPos(QPointF(n4_x, n4_y))


        #fils  #TODO : remplacer par classes et methodes

            #n1-n2
        f1_2 = scene.addLine(n1_x, n1_y, n2_x, n2_y, blackPen)
        f1_2.milieu_x = (n1_x+n2_x)/2
        f1_2.milieu_y = (n1_y+n2_y)/2

            #n2-n3
        f2_3 = scene.addLine(n2_x, n2_y, n3_x, n3_y, blackPen)
        f2_3.milieu_x = (n2_x+n3_x)/2
        f2_3.milieu_y = (n2_y+n3_y)/2

            #n3-n4
        f3_4 = scene.addLine(n3_x, n3_y, n4_x, n4_y, blackPen)
        f3_4.milieu_x = (n3_x+n4_x)/2
        f3_4.milieu_y = (n3_y+n4_y)/2

            #n4-n1
        f4_1 = scene.addLine(n4_x, n4_y, n1_x, n1_y, blackPen)
        f4_1.milieu_x = (n4_x+n1_x)/2
        f4_1.milieu_y = (n4_y+n1_y)/2

            #n1-n3
        f1_3 = scene.addLine(n1_x, n1_y, n3_x, n3_y, blackPen)
        f1_3.milieu_x = (n1_x+n3_x)/2
        f1_3.milieu_y = (n1_y+n3_y)/2


        #composants #TODO : remplacer par classes et methodes
            
            #générateur

        generateur_radius = 25
        generateur_diameter = generateur_radius*2

        generateur = scene.addEllipse(f1_2.milieu_x-generateur_radius, f1_2.milieu_y-generateur_radius, generateur_diameter, generateur_diameter, blackPen)
        generateur_text = scene.addText("G", QFont("Sanserif", 15))
        generateur_text.setPos(QPointF(f1_2.milieu_x+generateur_radius/2, f1_2.milieu_y+generateur_radius/2))

            #resistance 1

        resistance_largeur = 20
        resistance_longueur = 40


        resistance1 = scene.addRect(f2_3.milieu_x-resistance_longueur/2, f2_3.milieu_y-resistance_largeur/2, resistance_longueur, resistance_largeur, blackPen)
        resistance1.text = scene.addText("R1", QFont("Sanserif", 15))
        resistance1.text.setPos(QPointF(f2_3.milieu_x-resistance_longueur/2, f2_3.milieu_y+resistance_largeur/2))

            #resistance 2

        resistance2 = scene.addRect(f4_1.milieu_x-resistance_longueur/2, f4_1.milieu_y-resistance_largeur/2, resistance_longueur, resistance_largeur, blackPen)
        resistance2.text = scene.addText("R2", QFont("Sanserif", 15))
        resistance2.text.setPos(QPointF(f4_1.milieu_x-resistance_longueur/2, f4_1.milieu_y+resistance_largeur/2))

            #condensateur 1

        condensateur_longueur = 40
        condensateur_espacement = 5

        condensateur_l1_milieu_x = f1_3.milieu_x + condensateur_espacement
        condensateur_l1_milieu_y = f1_3.milieu_y - condensateur_espacement
        condensateur_l2_milieu_x = f1_3.milieu_x - condensateur_espacement
        condensateur_l2_milieu_y = f1_3.milieu_y + condensateur_espacement

        condensateur_l1=scene.addLine(condensateur_l1_milieu_x + condensateur_longueur/2 + condensateur_espacement, condensateur_l1_milieu_y,condensateur_l1_milieu_x - condensateur_longueur/2 - condensateur_espacement, condensateur_l1_milieu_y, blackPen)
        condensateur_l1.setTransformOriginPoint(condensateur_l1_milieu_x, condensateur_l1_milieu_y)
        condensateur_l1.setRotation(55)

        condensateur_l2=scene.addLine(condensateur_l2_milieu_x + condensateur_longueur/2 + condensateur_espacement, condensateur_l2_milieu_y,condensateur_l2_milieu_x - condensateur_longueur/2 - condensateur_espacement, condensateur_l2_milieu_y, blackPen)
        condensateur_l2.setTransformOriginPoint(condensateur_l2_milieu_x, condensateur_l2_milieu_y)
        condensateur_l2.setRotation(55)

            #inductance 1 #TODO faut faire quelques petits trucs là, notamment le soucis d'avoir 5 petits elements
        
        inductance_diametre = 16
        inductance_rayon = inductance_diametre/2
        inductance_decalage = inductance_rayon * 1.5

        inductance_1=scene.addEllipse(f3_4.milieu_x-inductance_rayon, f3_4.milieu_y-inductance_decalage, inductance_diametre, inductance_diametre, blackPen)
        inductance_2=scene.addEllipse(f3_4.milieu_x-inductance_rayon, f3_4.milieu_y, inductance_diametre, inductance_diametre, blackPen)
        inductance_3=scene.addEllipse(f3_4.milieu_x-inductance_rayon, f3_4.milieu_y+inductance_decalage, inductance_diametre, inductance_diametre, blackPen)


        def create_noeud(self, px, py, name):
            self.ellipse = scene.addEllipse(px, py, 5, 5, blackPen)
            self.ellipse.setFlag(QGraphicsItem.ItemIsMovable)

        def create_text():
            scene.addText("This is the greatest text, ever - Donald J. Trump", QFont("Sanserif", 15))
        

        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(0,0, max_size_x+100, max_size_y+100)


if __name__ == '__main__':
    pass

