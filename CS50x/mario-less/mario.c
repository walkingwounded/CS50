// Problem Set 1: Mario
// In this problem set, I've used do, for loop, else if conditions to print Mario pyramid bricks based on the height from get_int().

#include <cs50.h>
#include <stdio.h>

void print_brick(int i);

int main(void)
{
    int i;

    // do function to error check
    do
    {
        i = get_int("Height: ");
        print_brick(i);
    }
    while (i < 1);
}

// function for printing bricks.
// utilized for loop, and if + else conditions.
void print_brick(int i)
{
    int height;
    int width;
    int brick;

    for (height = i; height > 0; height--)
    {
        brick = 1;
        for (width = i; width > 0; width--)
        {
            if (height > brick)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
            brick++;
        }
        printf("\n");
    }
}
