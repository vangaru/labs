#include<iostream>
#include <vector>
#include <set>
#include <climits>

using namespace std;

class Graph {
private:
    // количество вершин
    int V;
    int E;
    vector<pair<int, int>> G; // граф исходный
    vector<pair<int, int>> D; // граф декодированный
    vector<int> Degree;
    vector<int> Code;
public:
    Graph(int v);
    void add_edge(int u, int v);
    void prufer_encode();
    void prufer_decode();
    void display();
};

Graph::Graph(int v) {
    V = v;
    E = V - 1;
    vector<int> d(V, 0);
    Degree = d;
    Code.clear();
    D.clear();
}

void Graph::add_edge(int u, int v) {
    G.push_back(make_pair(u, v));
    Degree[u]++;
    Degree[v]++;
}

void Graph::display() {
    cout << "Исходное дерево:\n";
    for (int i = 0; i < G.size(); i++) {
        cout << G[i].first << " " << G[i].second << "\n";
    }

    cout << "Код Прюфера: ";
    for (int i = 0; i < Code.size(); i++) {
        cout << Code[i] << " ";
    }
    cout << "\n";

    cout << "Декодированное дерево:\n";
    for (int i = 0; i < D.size(); i++) {
        cout << D[i].first << " " << D[i].second << "\n";
    }
}

void Graph::prufer_encode() {
    int x;
    for (int i = 0; i < V - 2; i++) {
        int min = INT_MAX;
        // выбрать вершину с наименьшим индексом и равную 1
        for (int j = 0; j < E; j++) {
            if (Degree[G[j].first] == 1 && Degree[G[j].second] > 0) {
                if (min > G[j].first) {
                    min = G[j].first;
                    x = j;
                }
            }
            if (Degree[G[j].second] == 1 && Degree[G[j].first] > 0) {
                if (min > G[j].second) {
                    min = G[j].second;
                    x = j;
                }
            }
        }
        // уменьшить значение вершин на 1
        if (Degree[G[x].first] > 0) {
            Degree[G[x].first]--;
        }
        if (Degree[G[x].second] > 0) {
            Degree[G[x].second]--;
        }

        // сохранить вершину, из которой удаляется лист
        if (Degree[G[x].first] == 0) {
            Code.push_back(G[x].second);
        }
        else {
            Code.push_back(G[x].first);
        }
    }
}

void Graph::prufer_decode() {
    int n = (int)Code.size() + 2;
    vector<int> degree(n, 1);
    for (int i = 0; i < n - 2; ++i) {
        ++degree[Code[i]];
    }

    set<int> leaves;
    for (int i = 0; i < n; ++i) {
        if (degree[i] == 1) {
            leaves.insert(i);
        }
    }

    for (int i = 0; i < n - 2; ++i) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());
        int v = Code[i];
        D.push_back(make_pair(leaf, v));
        if (--degree[v] == 1) {
            leaves.insert(v);
        }
    }
    D.push_back(make_pair(*leaves.begin(), *--leaves.end()));
}

int main() {
    setlocale(0, "");

    Graph gp(12);
    gp.add_edge(0, 1);
    gp.add_edge(0, 2);
    gp.add_edge(1, 3);
    gp.add_edge(1, 4);
    gp.add_edge(2, 5);
    gp.add_edge(2, 6);
    gp.add_edge(5, 7);
    gp.add_edge(7, 8);
    gp.add_edge(7, 9);
    gp.add_edge(9, 10);
    gp.add_edge(10, 11);

    gp.prufer_encode();
    gp.prufer_decode();
    gp.display();

    return 0;
#include<iostream>
#include <vector>
#include <set>
#include <climits>

using namespace std;

class Graph {
private:
    // количество вершин
    int V;
    int E;
    vector<pair<int, int>> G; // граф исходный
    vector<pair<int, int>> D; // граф декодированный
    vector<int> Degree;
    vector<int> Code;
public:
    Graph(int v);
    void add_edge(int u, int v);
    void prufer_encode();
    void prufer_decode();
    void display();
};

Graph::Graph(int v) {
    V = v;
    E = V - 1;
    vector<int> d(V, 0);
    Degree = d;
    Code.clear();
    D.clear();
}

void Graph::add_edge(int u, int v) {
    G.push_back(make_pair(u, v));
    Degree[u]++;
    Degree[v]++;
}

void Graph::display() {
    cout << "Исходное дерево:\n";
    for (int i = 0; i < G.size(); i++) {
        cout << G[i].first << " " << G[i].second << "\n";
    }

    cout << "Код Прюфера: ";
    for (int i = 0; i < Code.size(); i++) {
        cout << Code[i] << " ";
    }
    cout << "\n";

    cout << "Декодированное дерево:\n";
    for (int i = 0; i < D.size(); i++) {
        cout << D[i].first << " " << D[i].second << "\n";
    }
}

void Graph::prufer_encode() {
    int x;
    for (int i = 0; i < V - 2; i++) {
        int min = INT_MAX;
        // выбрать вершину с наименьшим индексом и равную 1
        for (int j = 0; j < E; j++) {
            if (Degree[G[j].first] == 1 && Degree[G[j].second] > 0) {
                if (min > G[j].first) {
                    min = G[j].first;
                    x = j;
                }
            }
            if (Degree[G[j].second] == 1 && Degree[G[j].first] > 0) {
                if (min > G[j].second) {
                    min = G[j].second;
                    x = j;
                }
            }
        }
        // уменьшить значение вершин на 1
        if (Degree[G[x].first] > 0) {
            Degree[G[x].first]--;
        }
        if (Degree[G[x].second] > 0) {
            Degree[G[x].second]--;
        }

        // сохранить вершину, из которой удаляется лист
        if (Degree[G[x].first] == 0) {
            Code.push_back(G[x].second);
        }
        else {
            Code.push_back(G[x].first);
        }
    }
}

void Graph::prufer_decode() {
    int n = (int)Code.size() + 2;
    vector<int> degree(n, 1);
    for (int i = 0; i < n - 2; ++i) {
        ++degree[Code[i]];
    }

    set<int> leaves;
    for (int i = 0; i < n; ++i) {
        if (degree[i] == 1) {
            leaves.insert(i);
        }
    }

    for (int i = 0; i < n - 2; ++i) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());
        int v = Code[i];
        D.push_back(make_pair(leaf, v));
        if (--degree[v] == 1) {
            leaves.insert(v);
        }
    }
    D.push_back(make_pair(*leaves.begin(), *--leaves.end()));
}

int main() {
    setlocale(0, "");

    Graph gp(12);
    gp.add_edge(0, 1);
    gp.add_edge(0, 2);
    gp.add_edge(1, 3);
    gp.add_edge(1, 4);
    gp.add_edge(2, 5);
    gp.add_edge(2, 6);
    gp.add_edge(5, 7);
    gp.add_edge(7, 8);
    gp.add_edge(7, 9);
    gp.add_edge(9, 10);
    gp.add_edge(10, 11);

    gp.prufer_encode();
    gp.prufer_decode();
    gp.display();

    return 0;
}