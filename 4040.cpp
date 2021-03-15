#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int total_period = 0, room = 0; //여름 성수기 총 기간, 방 개수
int checkIn = 0, checkOut = 0;
char temp[101][31];

int greedy(int index) {
    int maxCount = 0;

    for (int i = 0; i < room; i++) {
        int count = 0;
        for (int j = index; j < checkOut - 1; j++) {
            if (temp[j][i] == 'O') { count++; }
            else { break; }
        }
        if (maxCount < count) {
            maxCount = count;
        }
    }
    return maxCount;
}

int main() {
    
    cin >> total_period >> room;

    for (int i = 0; i < total_period; i++) {
        for (int j = 0; j < room; j++) {
            cin >> temp[i][j];
        }
    }

    cin >> checkIn >> checkOut;

    int change = -1;
    for (int i = checkIn - 1; i < checkOut - 1;) {
        change++;

        if (greedy(i) == 0) {
            change = -1;
            break;
        }
        i += greedy(i);
    }
    cout << change << endl;;
        
    }

