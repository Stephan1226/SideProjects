//
// Created by Stephan Kim on 11/12/24.
//
#include <stdio.h>
#include <stdlib.h>

int main () {
    int r, c;
    int memo[50][50];
    scanf("%d", &r, c);
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if(i == 0 || j == 0) {
          memo[i][j] = 1;
          break;
        }
        memo[i][j] = memo[i-1][j] + memo[i][j-1];
      }
    }
    printf("%d", memo[r-1][c-1]);
}
