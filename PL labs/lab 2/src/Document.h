#pragma once

class Document
{
protected:
	
	float date;
	int number;

public:

	virtual void infoOutput() = 0;

	struct Node {
		Document* document;
		Node* next;
	};

	static Node* head;

	void push();

	static void listOutput();


	void setDate(float date);
	void setNumber(int number);


	float getDate();
	int getNumber();

	Document(float date, int number);
	Document();
	virtual ~Document() {};
};

