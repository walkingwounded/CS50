// Problem set 2: Scrabble
// My approach for this challenge set was to get input from Player 1 & 2 and compare the points awarded through a point_system
// variable. The point_system(char *s) takes in string/array of chars and then return with points.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int point_system(char *s);

int main(void)
{
    char *string1;
    char *string2;
    int p1;
    int p2;

    string1 = get_string("Player 1: ");
    string2 = get_string("Player 2: ");

    p1 = point_system(string1);
    p2 = point_system(string2);

    if (p1 > p2)
        printf("Player 1 wins!\n");
    else if (p1 < p2)
        printf("Player 2 wins!\n");
    else
        printf("Tie!\n");

    return 1;
}

// point system to award points for string, used a counter and tolower() the array in the while loop.
// checks the strings with if conditions and return counter.
int point_system(char *s)
{
    int counter;

    counter = 0;
    while (*s != '\0')
    {
        *s = tolower(*s);
        if (*s < 'a' || *s > 'z')
            counter += 0;
        else if (*s == 'q' || *s == 'z')
            counter += 10;
        else if (*s == 'j' || *s == 'x')
            counter += 8;
        else if (*s == 'k')
            counter += 5;
        else if (*s == 'f' || *s == 'h' || *s == 'v' || *s == 'w' || *s == 'y')
            counter += 4;
        else if (*s == 'c' || *s == 'm' || *s == 'p')
            counter += 3;
        else if (*s == 'd' || *s == 'g' || *s == 'b')
            counter += 2;
        else
            counter += 1;
        s++;
        // to check counter
        //  printf("%d\n", counter);
    }
    return counter;
}
