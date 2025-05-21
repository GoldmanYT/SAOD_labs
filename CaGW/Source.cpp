#include <ctime>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

struct Point {
    int x, y;
};

const int max_size = 20;

void findSolution(int field[max_size][max_size], int n);
void getNextPoints(Point point, vector<Point>& dest, bool visited[max_size][max_size], int n);
bool isOnField(Point point, int n);

int field[max_size][max_size] = {};

int main()
{
    setlocale(LC_ALL, "Russian");
    srand(time(0));

    int n = 8;
#if 1
    cout << "Введите длину поля: ";
    cin >> n;
    cout << endl;
#endif
    cout << "Доска:" << endl;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
            field[x][y] = rand() % 100 + 1;
            cout << field[x][y] << "\t";
        }
        cout << endl;
    }

    findSolution(field, n);

    return 0;
}

void findSolution(int field[max_size][max_size], int n)
{
    bool visited[max_size][max_size] = {};
    visited[0][0] = 1;
    vector<Point> currentPath(1, { 0, 0 });
    vector<vector<Point>> notVisitedPoints = { vector<Point>() };
    getNextPoints(currentPath.back(), notVisitedPoints.back(), visited, n);
    int currentSum = field[0][0];
    vector<Point> bestPath;
    int minSum = INT_MAX;

    while (!currentPath.empty()) {
        while (!notVisitedPoints.back().empty() && currentSum < minSum) {
            Point nextPoint = notVisitedPoints.back().back();
            notVisitedPoints.back().pop_back();
            currentPath.push_back(nextPoint);
            currentSum += field[nextPoint.x][nextPoint.y];
            visited[nextPoint.x][nextPoint.y] = 1;
            if (nextPoint.x == n - 1 && nextPoint.y == n - 1 && currentSum < minSum) {
                minSum = currentSum;
                bestPath = currentPath;
            }
            notVisitedPoints.push_back(vector<Point>());
            getNextPoints(nextPoint, notVisitedPoints.back(), visited, n);
        }
        Point& lastPoint = currentPath.back();
        visited[lastPoint.x][lastPoint.y] = 0;
        currentSum -= field[lastPoint.x][lastPoint.y];
        currentPath.pop_back();
        notVisitedPoints.pop_back();
    }
    cout << "Сумма: " << minSum << endl;
    cout << "Путь: ";
    for (auto& point : bestPath) {
        cout << "(" << point.x + 1 << ", " << point.y + 1 << ") ";
    }
}

void getNextPoints(Point point, vector<Point>& dest, bool visited[max_size][max_size], int n)
{
    for (int scaleX = 1; scaleX <= 2; scaleX++) {
        for (int dx = -scaleX; dx <= scaleX; dx += 2 * scaleX) {
            int scaleY = 3 - scaleX;
            for (int dy = -scaleY; dy <= scaleY; dy += 2 * scaleY) {
                Point nextPoint = { point.x + dx, point.y + dy };
                if (isOnField(nextPoint, n) && !visited[nextPoint.x][nextPoint.y]) {
                    dest.push_back(nextPoint);
                }
            }
        }
    }
}

bool isOnField(Point point, int n)
{
    return 0 <= point.x && point.x < n && 0 <= point.y && point.y < n;
}