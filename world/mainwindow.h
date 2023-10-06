#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <QObject>
#include <QMainWindow>
#include <QFileDialog>
#include <QDebug>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    const QChar english[17] ={'e', 't', 'a',  'o', 'i',  'n',  's', 'h', 'r', 'd', 'l', 'c', 'u', 'm',  'w',  'f',  'g'};
    const QString zentil[17]={"a-","z-","eh-","i-","uh-","rr-","n-","s-","l-","v-","t-","m-","o-","th-","k-", "sh-","f-"};

    const QList<QString> end2{"ed","er"};
    const QList<QString> end3{"ion","ing"};
    const QList<QList<QString>> endAll{end2,end3};

    const QList<QString> r1L1{"y", "da"};
    const QList<QString> r2L1{"p", "te"};
    const QList<QString> r3L1{"b", "mo"};
    const QList<QString> r4L1{"v", "to"};
    const QList<QString> r5L1{"k", "na"};
    const QList<QString> r6L1{"j", "wa"};
    const QList<QString> r7L1{"x", "on"};
    const QList<QString> r8L1{"p", "mu"};
    const QList<QString> r9L1{"z", "hi"};

    const QList<QString> r1L2{"cc", "c"};
    const QList<QString> r2L2{"ll", "l"};
    const QList<QString> r3L2{"sh", "s"};
    const QList<QString> r4L2{"th", "t"};
    const QList<QString> r5L2{"oo", "o"};
    const QList<QString> r6L2{"nn", "n"};
    const QList<QString> r7L2{"tt", "fin"};
    const QList<QString> r8L2{"ee", "e"};
    const QList<QString> r9L2{"rr", "r"};
    const QList<QString> r10L2{"kn", "k"};

    const QList<QString> r1L3{"ght", "gt"};

    const QList<QList<QString>> replace1{r1L1, r2L1, r3L1, r4L1, r5L1, r6L1, r7L1, r8L1, r9L1};
    const QList<QList<QString>> replace2{r1L2, r2L2, r3L2, r4L2, r5L2, r6L2, r7L2, r8L2, r9L2, r10L2};
    const QList<QList<QString>> replace3{r1L3};
    const QList<QList<QList<QString>>> replaceAll{replace1, replace2,replace3};

    MainWindow(QWidget *parent = nullptr);
    void convert();
    void letterDisplay(const QList<QString> &eng);
    ~MainWindow();

private slots:
    void on_engOut_textChanged();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
