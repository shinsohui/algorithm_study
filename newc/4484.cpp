#include<iostream>
#include<algorithm>
#include<deque>
using namespace std;

int main(){
    int N;
    cin >> N;

    deque<int> lock(N);
    int num;
    for(int i = 0; i < N; i++)
        cin >> lock[i];

    int rotate2 = 0;
    for(int i = 0; i < N; i++){
        if(lock[N - 1] - lock[N - 2] != 1){
            lock.push_front(lock.back());
            lock.pop_back();
            rotate2++;
        }
        else break;
    }
    if(rotate2 == 0) rotate2 = N;
    // 마지막 원소 맨 앞에 넣기
    lock.push_front(lock.back());
    // 첫번째 원소를 맨 뒤에 넣기
    lock.push_back(lock[1]); // 지금 deque에 있는 총 원소수는 N + 2

    int tmp = 0;
    int endIdx = -1;
    for(int i = 1; i <= N; i++){
        if(lock[i] - lock[i - 1] != 1 && lock[i + 1] - lock[i] != 1){
            tmp++;
            endIdx = i;
        }
    }
    int startIdx = endIdx - tmp + 1;

    reverse(lock.begin() + startIdx, lock.begin() + endIdx + 1);

    int rotate1 = 0;
    for(int i = 1; i <= N; i++){
        if(lock[i] == 1){
            rotate1 = N + 1 - i;
            break;
        }
    }

    cout << rotate1 << '\n';
    cout << startIdx << ' ' << endIdx << '\n';
    cout << rotate2;

    return 0;
}
