#include "menu.h"

#include "Cube.h"
#include "Cylinder.h"
#include "Tetrahedron.h"
#include "Container.h"

#include <iostream>

using namespace std;

/*
  1 - ����� �������
  2 - ����� �������� �� �������
  3 - �������� �������� �������
  4 - ���������� �������� � ������
  5 - ��������� �����
  6 - �����
*/

void menu() {

	Container* container = Container::containerInitialize();

	Cube* cube1;
	Cube* cube2;

	int choice;
	do {
		cout << endl;
		cout << "1 - ����� �������\n";
		cout << "2 - ����� �������� �� �������\n";
		cout << "3 - �������� �������� �������\n";
		cout << "4 - ���������� �������� � ������\n";
		cout << "5 - ��������� �����\n";
		cout << "6 - ������������ ������ ��������� '='\n";
		cout << "7 - �����\n";
		cout << "\n�������� �������� >>> ";

		cin >> choice;

		cout << endl;

		switch (choice) {

		case 1:
			container->containerOutput();
			break;

		case 2:
			cout << "\n������� ������ �������� ��� ������ >>> ";

			int index;
			cin >> index;
			try {
				if (index < 0 || index >= container->getSize()) {
					throw(index);
				}

				container->operator[](index)->infoOutput();
			}
			catch (int) {
				cout << "\n������ " << index << " ������� �� ������� �������\n";
			}

			break;

		case 3:
			cout << "\n������� ������ �������� ��� �������� >>> ";

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
				cout << "\n������ " << delIndex << " ������� �� ������� �������\n";
			}

			break;

		case 4:
			cout << "\n������� ������ �������� ��� ������� >>> ";

			int insertIndex;
			cin >> insertIndex;

			try {

				if (insertIndex < 0 || insertIndex > container->getSize()) {
					throw(insertIndex);
				}

				cout << "1 - ���\n";
				cout << "2 - �������\n";
				cout << "3 - ��������\n";
				cout << "\n�������� ������ >>> ";

				int figure;
				cin >> figure;

				switch (figure) {
				case 1:
					cout << "\n������� ����� ����� ���� >>> ";
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
					cout << "\n������� ������ �������� >>> ";
					float height;
					cin >> height;

					cout << "\n������� ������ ��������� �������� >>> ";
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
					cout << "\n������� ����� ����� ��������� >>> ";
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
					cout << "\n �������� ����!!! \n";
					break;
				}

			}
			catch (int) {
				cout << "\n������ " << insertIndex << " ������� �� ������� �������\n";
			}

			break;

		case 5:
			cout << "\n������� ����� ����� 1 ���� >>> ";
			int cubeEdgeLength1;
			cin >> cubeEdgeLength1;

			cout << "\n������� ����� ����� 2 ���� >>> ";
			int cubeEdgeLength2;
			cin >> cubeEdgeLength2;

			cube1 = new Cube(cubeEdgeLength1);
			cube2 = new Cube(cubeEdgeLength2);

			if (cube1->operator==(*cube2)) {
				cout << "\n���� �����\n";
			}
			else {
				cout << "\n���� �� �����\n";
			}

			break;

		case 6:
			cout << "\n������� ����� ����� ���� >>> ";

			int len;
			cin >> len;

			cube1 = new Cube(len);
			cube2 = new Cube();
			cube2->operator=(*cube1);

			cout << "\n������ ���:\n" << cube1;
			cube1->infoOutput();

			cout << "\n������ ���:\n" << cube2;
			cube2->infoOutput();

			break;

		case 7:
			break;

		default:
			break;
		}
	} while (choice != 7);
}
