#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QSplitter>
#include <QLineEdit>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
	ui->setupUi(this);

	// Connect the textChanged signal to the custom slot
	connect(ui->engOut, &QTextEdit::textChanged, this, [this]() {
    	this->convert(); 
	});
	//QSplitter* langSplitter = new QSpliter();
	//QSplitter* graphSplitter = new QSpliter();
}

MainWindow::~MainWindow() {
	delete ui;
}

void MainWindow::convert(){
	const QString engWord = ui->engOut->toPlainText();
	QList<QString> engSen;
	QString zenWord;

	// Transforms the imputed sentence into a QList of Qstings
	int sepIndx = 0;
	while (sepIndx < engWord.length()) {
		int tmpIndx = engWord.indexOf(' ', sepIndx);
		if (tmpIndx == -1)
			tmpIndx = engWord.length();
		QString tmpWord = engWord.sliced(sepIndx, tmpIndx-sepIndx);
		engSen.append(tmpWord);
		sepIndx = tmpIndx + 1;
	}

	// Edits the word depending on replaceAll and endAll list in mainwindow.h
	for (int t = 0;t <engSen.length(); ++t){
		//the word that we will be working on
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
		// replaces unwanted combinations via replaceAll list
		for (int i=1; i <= 3; ++i){
			for (size_t j=0; j < replaceAll[i-1].size(); ++j){
				int index = 0;
				while (index < word.length()){
					index = word.indexOf(replaceAll[i-1][j][0], index);
					if (index == -1)
						break;
					word.replace(index,i, replaceAll[i-1][j][1]);
					index += i;
				}
			}
		}
		// Save changes to engSen
		engSen.replace(t, word);

		// convert
		for (size_t i=0; i < word.length(); ++i){
			for (int j=0; j < 17; ++j){
				if (word[i] == english[j]){
					zenWord.append(zentil[j]);
				}
			}
		}
		zenWord.replace(zenWord.length()-1,1,"	");
	}
	zenWord.chop(2);
	ui->zenOut->setText(zenWord);
	// letters display
	if (ui->graphicsView->scene())
		ui->graphicsView->scene()->clear();
	letterDisplay(engSen);
}

void MainWindow::letterDisplay(const QList<QString> &eng) {
	const QPixmap a("../world/letters/a.png");
	const QPixmap eh("../world/letters/eh.png");
	const QPixmap f("../world/letters/f.png");
	const QPixmap i("../world/letters/i.png");
	const QPixmap k("../world/letters/k.png");
	const QPixmap l("../world/letters/l.png");
	const QPixmap m("../world/letters/m.png");
	const QPixmap n("../world/letters/n.png");
	const QPixmap o("../world/letters/o.png");
	const QPixmap rr("../world/letters/rr.png");
	const QPixmap s("../world/letters/s.png");
	const QPixmap sh("../world/letters/sh.png");
	const QPixmap t("../world/letters/t.png");
	const QPixmap th("../world/letters/th.png");
	const QPixmap uh("../world/letters/uh.png");
	const QPixmap v("../world/letters/v.png");
	const QPixmap z("../world/letters/z.png");

	const QList imgList = {a,z,eh,i,uh,rr,n,s,l,v,t,m,o,th,k,sh,f};

	QPixmap empty(a.width(), a.height());
	empty.fill(Qt::transparent);
	int width = 0;
	for (int listIndx=0; listIndx<eng.length(); ++listIndx){
		for (int letterIndx=0; letterIndx<eng.at(listIndx).length(); ++letterIndx){
			for (int alph=0; alph<17; ++alph){
				if (eng.at(listIndx).at(letterIndx) == english[alph]) {
					width += imgList.at(alph).width() -2;
				}
			}
		}
		width += a.width();
	}
	QPixmap disp(width, a.height());
	disp.fill(Qt::transparent);
	QPainter painter(&disp);
	width=0;
	for (int listIndx=0; listIndx<eng.length(); ++listIndx){
		for (int letterIndx=0; letterIndx<eng.at(listIndx).length(); ++letterIndx){
			for (int alph=0; alph<17; ++alph){
				if (eng.at(listIndx).at(letterIndx) == english[alph]) {
					painter.drawPixmap(width,0,imgList.at(alph));
					width += imgList.at(alph).width() -2;
				}
			}
		}
		painter.drawPixmap(width,0,empty);
		width += a.width();
	}

	if (! ui->graphicsView->scene()) {
		qDebug() << "No Scene!";

		QGraphicsScene *scene = new QGraphicsScene(this);
		ui->graphicsView->setScene(scene);
	}

	ui->graphicsView->scene()->addPixmap(disp.scaled(disp.width()/2,disp.height()/2));
}
