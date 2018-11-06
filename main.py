from pygments.lexers import CLexer
import os, sys

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout

from kivy.uix.codeinput import CodeInput


list = ['\MinGW\\bin\libgcc_s_dw2-1.dll', '\MinGW\\bin\libstdc++-6.dll']


helloworld = """#include <cstdlib>
#include <iostream>
using namespace std;

int main() 
{
	cout << "Hello, World!";
	system("pause");
	return 0;
}"""

cycles = """#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    //int i; счетчик цикла
    int sum = 0; // сумма чисел от 0 до 1000.
    setlocale(0, "");
    for (int i = 0; i <= 1000; i++) // задаем начальное значение 1, конечное 1000 и задаем шаг цикла - 1.
    {
        sum = sum + i;
    }
    cout << "Сумма чисел от 1 до 1000 = " << sum << endl;        
    system("pause"); 
    return 0;
}
"""

array = """#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main()    
{
    string students[10] = {
        "Иванов", "Петров", "Сидоров",
        "Петров", "Ерошкин", "Выхин",
        "Андеев", "Вин Дизель", "Картошкин", "Васечкин"
    };
    cout << students << endl; // Пытаемся вывести весь массив непосредственно
    system("pause");
    return 0;
}"""

datatypes = """#include <cstdlib>
#include <iostream> 
using namespace std;

int main() 
{ 
    setlocale(0, ""); 
    /*7*/ int a, b; // объявление двух переменных a и b целого типа данных. 
    cout << "Введите первое число: "; 
    cin >> a; // пользователь присваивает переменной a какое-либо значение. 
    cout << "Введите второе число: "; 
    cin >> b; 
    /*12*/  int c = a + b; // новой переменной c присваиваем значение суммы введенных пользователем данных. 
    cout << "Сумма чисел = " << c << endl; // вывод ответа.
    system("pause");
    return 0; 
}"""

functionscpp = """#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main()
{    
    string valid_pass = "qwerty123";
    string user_pass;
    cout << "Введите пароль: ";
    getline(cin, user_pass);
    if (user_pass == valid_pass) {
        cout << "Доступ разрешен." << endl;
    } else {
        cout << "Неверный пароль!" << endl;
    }
    system("pause");
    return 0;    
}"""

pointers = """//Пример использования статических переменных
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    int a; // Объявление статической переменной
    int b = 5; // Инициализация статической переменной b

    a = 10;
    b = a + b;
    cout << "b is " << b << endl;
    system("pause");
    return 0;
}

//Пример использования динамических переменных
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    int *a = new int; // Объявление указателя для переменной типа int
    int *b = new int(5); // Инициализация указателя

    *a = 10;
    *b = *a + *b;

    cout << "b is " << *b << endl;

    delete b;
    delete a;
    
    system("pause");
    return 0;
}"""

classes = """#include <cstdlib>
#include <iostream>
using namespace std;
// начало объявления класса
class CppStudio // имя класса
{
public: // спецификатор доступа
    void message() // функция (метод класса) выводящая сообщение на экран
    {
        cout << "website: cppstudio.com\ntheme: Classes and Objects in C + +\n";
    }
}; // конец объявления класса CppStudio
 
int main(int argc, char* argv[])
{
    CppStudio objMessage; // объявление объекта
    objMessage.message(); // вызов функции класса message
    system("pause");
    return 0;
}"""

class MyApp(App):
    def build(self):
        self.ScreenManager = ScreenManager()
        self.sc1 = Screen(name='firstscreen')
        self.sc2 = Screen(name='secscreen')

        self.file_dir = ''
        self.file_name = ''

        self.compile = Button(text='Скомпилировать', on_press=self.CompileCPP)
        self.run = Button(text='Запустить', on_press=self.StartEXE)

        self.dropdown = DropDown()
        self.btn1 = Button(text='Сохранить как', size_hint_y=None, height=30, on_press=self.SaveAsFile)
        self.btn2 = Button(text='Сохранить', size_hint_y=None, height=30, on_press=self.SaveAs)
        self.btn3 = Button(text='Открыть файл', size_hint_y=None, height=30, on_press=self.ReadFromFile)
        self.btn4 = Button(text='Подсказки', size_hint_y=None, height=30, on_press=self.secrets)

        self.btn1.bind()

        self.secscrbutt1 = Button(text='Назад', size_hint_y=None, pos_hint={'top': 1}, height=30, on_press=self.MainWindow)

        self.secscrBox = BoxLayout()
        self.secscrBox.add_widget(self.secscrbutt1)
        self.secscrAnch = AnchorLayout(anchor_y='top')
        self.secscrAnch.add_widget(self.secscrBox)

        self.secscrtext = CodeInput(text="", lexer=CLexer())
        self.secscrBox2 = BoxLayout(size_hint=[.8, .953])
        self.secscrBox2.add_widget(self.secscrtext)
        self.secscrAnch2 = AnchorLayout(anchor_y='bottom', anchor_x='right')
        self.secscrAnch2.add_widget(self.secscrBox2)

        self.pod1 = Button(text='Hello World!', on_press=self.Tips)
        self.pod2 = Button(text='Типы данных', on_press=self.Tips)
        self.pod3 = Button(text='Циклы', on_press=self.Tips)
        self.pod4 = Button(text='Массивы', on_press=self.Tips)
        self.pod5 = Button(text='Функции', on_press=self.Tips)
        self.pod6 = Button(text='Указатели', on_press=self.Tips)
        self.pod7 = Button(text='Классы', on_press=self.Tips)


        self.secscrBox3 = BoxLayout(orientation='vertical', size_hint=[.2, .953], spacing=1)
        self.secscrAnch3 = AnchorLayout(anchor_y='bottom', anchor_x='left')
        self.secscrBox3.add_widget(self.pod1)
        self.secscrBox3.add_widget(self.pod2)
        self.secscrBox3.add_widget(self.pod3)
        self.secscrBox3.add_widget(self.pod4)
        self.secscrBox3.add_widget(self.pod5)
        self.secscrBox3.add_widget(self.pod6)
        self.secscrBox3.add_widget(self.pod7)

        self.secscrAnch3.add_widget(self.secscrBox3)

        self.dropdown.add_widget(self.btn1)
        self.dropdown.add_widget(self.btn2)
        self.dropdown.add_widget(self.btn3)
        self.dropdown.add_widget(self.btn4)

        self.fileButton = Button(text='Меню')

        self.fileButton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.fileButton, 'text', x))

        self.MyText = CodeInput(text="", lexer=CLexer())
        self.MyBox = BoxLayout(orientation='horizontal', size_hint=[1, .07])
        self.MyBox.add_widget(self.fileButton)
        self.MyBox.add_widget(self.compile)
        self.MyBox.add_widget(self.run)

        self.MyBox2 = BoxLayout(size_hint=[1, .93])
        self.MyBox2.add_widget(self.MyText)

        self.MyAnchor = AnchorLayout(anchor_y='top', anchor_x='left')
        self.MyAnchor2 = AnchorLayout(anchor_y='bottom')
        self.MyAnchor.add_widget(self.MyBox)
        self.MyAnchor2.add_widget(self.MyBox2)

        self.OAnchor = AnchorLayout()
        self.OAnchor.add_widget(self.MyAnchor)
        self.OAnchor.add_widget(self.MyAnchor2)

        self.sc1.add_widget(self.OAnchor)

        self.sc2.add_widget(self.secscrAnch)
        self.sc2.add_widget(self.secscrAnch2)
        self.sc2.add_widget(self.secscrAnch3)

        self.ScreenManager.add_widget(self.sc1)
        self.ScreenManager.add_widget(self.sc2)

        return self.ScreenManager

    def secrets(self, instance):
        self.ScreenManager.current = 'secscreen'

    def MainWindow(self, instance):
        self.ScreenManager.current = 'firstscreen'

    def ReadFromFile(self, instance):
        try:
            from tkinter import Tk
            from tkinter import filedialog as fd

            root = Tk()
            root.withdraw()
            self.file_dir = fd.askopenfilename()
            self.file_name = os.path.basename(self.file_dir)
            print(self.file_name)
            print(self.file_dir)
            f = open(self.file_dir)
            self.MyText.text = f.read()
            f.close()
        except:
            print('Файл не выбран')

    def SaveAsFile(self, instance):
        try:
            from tkinter import Tk
            from tkinter import filedialog as fd

            root = Tk()
            root.withdraw()
            self.file_dir = fd.asksaveasfilename(
                filetypes=(("CPP files", "*.cpp"), ("All files", "*.*")))
            f = open(self.file_dir, 'w')
            f.write(self.MyText.text)
            f.close()
            for name in list:
                os.system('cp ' + sys.path[0] + name + ' ' + self.file_dir)
        except:
            print('Файл не сохранён')

    def SaveAs(self, instance):
        if self.file_dir != '':
            try:
                f = open(self.file_dir, 'w')
                f.write(self.MyText.text)
                f.close()
                print('Сохранено')
            except:
                print('Файл не был сохранён')
        if self.file_dir == '':
            self.SaveAsFile(instance)

    def CompileCPP(self, instance):
        self.SaveAs(instance)
        self.path = sys.path[0]
        print(self.path)
        os.chdir('/MinGW/bin')
        os.system('g++ ' + self.file_dir + ' -o ' + self.file_dir[:-4] + '.exe')
        print('На вывод: g++ ' + self.file_dir + ' -o ' + self.file_dir[:-4] + '.exe')
        print('Компиляция завершена!')

    def StartEXE(self, instance):
        self.CompileCPP(instance)
        print(self.file_dir[:-4] + '.exe')
        string = self.file_dir[:-4] + '.exe'
        os.startfile(string)

    def Tips(self, instance):
        print(instance.text)
        if instance.text == 'Hello World!':
            self.secscrtext.text = helloworld
        if instance.text == 'Циклы':
            self.secscrtext.text = cycles
        if instance.text == 'Массивы':
            self.secscrtext.text = array
        if instance.text == 'Типы данных':
            self.secscrtext.text = datatypes
        if instance.text == 'Функции':
            self.secscrtext.text = functionscpp
        if instance.text == 'Указатели':
            self.secscrtext.text = pointers
        if instance.text == 'Классы':
            self.secscrtext.text = classes



if __name__ == "__main__":
    MyApp().run()
