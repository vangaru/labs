#include "menu.h"

#include "Cube.h"
#include "Cylinder.h"
#include "Tetrahedron.h"
#include "Container.h"

#include <iostream>

using namespace std;

/*
  1 - вывод массива
  2 - вывод элемента по индексу
  3 - удаление элемента массива
  4 - добавление элемента в массив
  5 - сравнение кубов
  6 - выход
*/

void menu() {

	Container* container = Container::containerInitialize();

	Cube* cube1;
	Cube* cube2;

	int choice;
	do {
		cout << endl;
		cout << "1 - вывод массива\n";
		cout << "2 - вывод элемента по индексу\n";
		cout << "3 - удаление элемента массива\n";
		cout << "4 - добавление элемента в массив\n";
		cout << "5 - сравнение кубов\n";
		cout << "6 - демонстрация работы оператора '='\n";
		cout << "7 - выход\n";
		cout << "\nВЫБЕРИТЕ ДЕЙСТВИЕ >>> ";

		cin >> choice;

		cout << endl;

		switch (choice) {

		case 1:
			container->containerOutput();
			break;

		case 2:
			cout << "\nВведите индекс элемента для вывода >>> ";

			int index;
			cin >> index;
			try {
				if (index < 0 || index >= container->getSize()) {
					throw(index);
				}

				container->operator[](index)->infoOutput();
			}
			catch (int) {
				cout << "\nИндекс " << index << " выходит за пределы массива\n";
			}

			break;

		case 3:
			cout << "\nВведите индекс элемента для удаления >>> ";

			int delIndex;
			cin >> delIndex;

			try {

				if (delIndex < 0 || delIndex >= container->getSize()) {
					throw(delIndex);
				}

				if (delIndex == container->getSize() - 1) {
					container->delete_back();
				}
				else {
					container->index_delete(delIndex);
				}

			}
			catch (int) {
				cout << "\nИндекс " << delIndex << " выходит за пределы массива\n";
			}

			break;

		case 4:
			cout << "\nВведите индекс элемента для вставки >>> ";

			int insertIndex;
			cin >> insertIndex;

			try {

				if (insertIndex < 0 || insertIndex > container->getSize()) {
					throw(insertIndex);
				}

				cout << "1 - КУБ\n";
				cout << "2 - ЦИЛИНДР\n";
				cout << "3 - ТЕТРАЕДР\n";
				cout << "\nВыберите фигуру >>> ";

				int figure;
				cin >> figure;

				switch (figure) {
				case 1:
					cout << "\nВведите длину ребра куба >>> ";
					float edgeLength;
					cin >> edgeLength;

					if (insertIndex == container->getSize()) {
						container->push_back(new Cube(edgeLength));
					}
					else {
						container->insert(new Cube(edgeLength), insertIndex);
					}

					break;

				case 2:
					cout << "\nВведите высоту цилиндра >>> ";
					float height;
					cin >> height;

					cout << "\nВведите радиус основания цилиндра >>> ";
					float baseRadius;
					cin >> baseRadius;

					if (insertIndex == container->getSize()) {
						container->push_back(new Cylinder(height, baseRadius));
					}
					else {
						container->insert(new Cylinder(height, baseRadius), insertIndex);
					}

					break;

				case 3:
					cout << "\nВведите длину ребра тетраедра >>> ";
					float edgeLengthTetrahedron;
					cin >> edgeLengthTetrahedron;

					if (insertIndex == container->getSize()) {
						container->push_back(new Tetrahedron(edgeLengthTetrahedron));
					}
					else {
						container->insert(new Tetrahedron(edgeLengthTetrahedron), insertIndex);
					}

					break;

				default:
					cout << "\n НЕВЕРНЫЙ ВВОД!!! \n";
					break;
				}

			}
			catch (int) {
				cout << "\nИндекс " << insertIndex << " выходит за пределы массива\n";
			}

			break;

		case 5:
			cout << "\nВведите длину ребра 1 куба >>> ";
			int cubeEdgeLength1;
			cin >> cubeEdgeLength1;

			cout << "\nВведите длину ребра 2 куба >>> ";
			int cubeEdgeLength2;
			cin >> cubeEdgeLength2;

			cube1 = new Cube(cubeEdgeLength1);
			cube2 = new Cube(cubeEdgeLength2);

			if (cube1->operator==(*cube2)) {
				cout << "\nКубы равны\n";
			}
			else {
				cout << "\nКубы не равны\n";
			}

			break;

		case 6:
			cout << "\nВведите длину ребра куба >>> ";

			int len;
			cin >> len;

			cube1 = new Cube(len);
			cube2 = new Cube();
			cube2->operator=(*cube1);

			cout << "\nПервый куб:\n" << cube1;
			cube1->infoOutput();

			cout << "\nВторой куб:\n" << cube2;
			cube2->infoOutput();

			break;

		case 7:
			break;

		default:
			break;
		}
	} while (choice != 7);
}
