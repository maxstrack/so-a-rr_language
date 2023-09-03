#include "mainwindow.h"
#include "./ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);

    //QObject::connect();
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::on_engOut_textEdited(const QString &arg1) {
    convert();
}

void MainWindow::convert(){
    //sorted via most reoccurring
    const QChar english[26] = {'e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z'};
    const QString zentil[26] = {"a-","z-","eh-","i-","uh-","rr-","n-","s-","l-","v-","t-","m-","o-","th-","k-", "sh-","f-","veh-","za-","mi-","zi-","rreh-","ke-","irr-","tho-","so-"};

    const std::vector<QString> end2{"ed","er"};
    const std::vector<QString> end3{"ion","ing"};
    const std::vector<std::vector<QString>> endAll{end2,end3};

    const std::vector<QString> search2{"cc","ll","sh","th","oo","nn","tt","ee","rr","kn","wh"};
    const std::vector<QString> search3{"ght"};
    const std::vector<std::vector<QString>> searchAll{search2,search3};


    const QString engWord = ui->engOut->text();
    QList<QString> engSen;
    QString zenWord;
    int sepIndx = 0;
    //QString word;
    while (sepIndx < engWord.length()) {
        int tmpIndx = engWord.indexOf(' ', sepIndx);
        if (tmpIndx == -1)
            tmpIndx = engWord.length();
        //engSen.append(engWord.sliced(sepIndx, tmpIndx-sepIndx));
        QString tmpWord = engWord.sliced(sepIndx, tmpIndx-sepIndx);
        engSen.append(tmpWord);
        sepIndx = tmpIndx + 1;
    }

    for (int t = 0;t <engSen.length(); ++t){
        QString word = engSen.at(t);
        // trim the ending depending on the endAll list
        if (word.length() > 4){
            for (int i=2; i <= 3; ++i){
                for (size_t j=0; j < endAll[i-2].size(); ++j){
                    if (word.endsWith(endAll[i-2][j]))
                        word.resize(word.length()-i);
                }
            }
        }

        // clears unwanted combinations
        for (int i=2; i <= 3; ++i){
            for (size_t j=0; j < searchAll[i-2].size(); ++j){
                int index = 0;
                while (index < word.length()){
                    index = word.indexOf(searchAll[i-2][j], index);
                    if (index == -1)
                        break;
                    word.remove(index+1,1);
                    index += i;
                }
            }
        }
        engSen.replace(t, word);

        // convert
        for (size_t i=0; i < word.length(); ++i){
            for (int j=0; j < 26; ++j){
                if (word[i] == english[j]){
                    zenWord.append(zentil[j]);
                }
            }
        }
        zenWord.replace(zenWord.length()-1,1,"  ");
    }
    zenWord.chop(2);
    ui->zenOut->setText(zenWord);
    // letters display
    if (ui->graphicsView->scene())
        ui->graphicsView->scene()->clear();
    letterDisplay(engSen);
}

void MainWindow::letterDisplay(const QList<QString> &eng) {
    QPixmap a("../letters/a.png");
    QPixmap eh("../letters/eh.png");
    QPixmap f("../letters/f.png");
    QPixmap i("../letters/i.png");
    QPixmap k("../letters/k.png");
    QPixmap l("../letters/l.png");
    QPixmap m("../letters/m.png");
    QPixmap n("../letters/n.png");
    QPixmap o("../letters/o.png");
    QPixmap rr("../letters/rr.png");
    QPixmap s("../letters/s.png");
    QPixmap sh("../letters/sh.png");
    QPixmap t("../letters/t.png");
    QPixmap th("../letters/th.png");
    QPixmap uh("../letters/uh.png");
    QPixmap v("../letters/v.png");
    QPixmap z("../letters/z.png");

    QList imgList = {a,z,eh,i,uh,rr,n,s,l,v,t,m,o,th,k,sh,f};
    const QChar english[26] = {'e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z'};

    QPixmap disp(14*a.width(), a.height());
    disp.fill(Qt::transparent);
    QPainter painter(&disp);
    int width=0;
    for (int listIndx=0; listIndx<eng.length(); ++listIndx){
        for (int letterIndx=0; letterIndx<eng.at(listIndx).length(); ++letterIndx){
            for (int alph=0; alph<26; ++alph){
                if (eng.at(listIndx).at(letterIndx) == english[alph] && alph<17) {
                    painter.drawPixmap(width,0,imgList.at(alph));
                    width += imgList.at(alph).width() -2;
                }
            }
        }
    }

    if (! ui->graphicsView->scene()) {
        qDebug() << "No Scene!";

        QGraphicsScene *scene = new QGraphicsScene(this);
        ui->graphicsView->setScene(scene);
    }

    ui->graphicsView->scene()->addPixmap(disp.scaled(disp.width()/2,disp.height()/2));
}
