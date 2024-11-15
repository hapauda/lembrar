#include <stdio.h>

void draw(int n);

int main(void)
{
    draw(1);
    return 0;
}

void draw(int n)
{
    if (n >10){
        return;
    }
    for (int i = 0; i < n ; i++)
    {
        printf("#");
    }
    printf("\n");

    draw(n +1);
}