// Laser typeshi
#include <bits/stdc++.h>
using namespace std;

int main(){
    cout << "Enter rows and columns: ";
    int R, C;
    cin >> R;
    cin >> C;
    cout << "Enter the grid:\n";
    vector<vector<char>> grid(R, vector<char>(C));
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            cin >> grid[i][j];
        }
    }
    int r = 0, c = 0;
    int dir = 0; // 0=Right, 1=Down, 2=Left, 3=Up
    vector<vector<vector<bool>>> visited(R, vector<vector<bool>>(C, vector<bool>(4, false)));
    int dr[] = {0, 1, 0, -1};
    int dc[] = {1, 0, -1, 0};

    while(true){
        if(visited[r][c][dir]) {
            cout << "TRAPPED";
            return 0;
        }
        visited[r][c][dir] = true;
        char ch = grid[r][c];
        if(ch == '/'){
            if(dir == 0) dir = 3;
            else if(dir == 1) dir = 2;
            else if(dir == 2) dir = 1;
            else if(dir == 3) dir = 0;
        } else if(ch == '\\'){ // because a single '\' is an escape character. 
            if(dir == 0) dir = 1;
            else if(dir == 1) dir = 0;
            else if(dir == 2) dir = 3;
            else if(dir == 3) dir = 2;
        }
        r += dr[dir];
        c += dc[dir];
        if(r < 0 || r >= R || c < 0 || c >= C){
            cout << "Exit coordinates: " << r << " " << c << "\n";
            return 0;
        }
    }
    return 0;
}