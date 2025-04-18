//  Problem set 1: Cash
//  Cash expects the number of coins leftover from a transaction. the coins denominators are 25, 10, 5, 1.
//  Utilized while loops to iterate through the input value "Change owed", and count the coins after each loop.
//  It is possible to code this using 1x while loop and mutliple if else with % modulus.

#include <cs50.h>
#include <stdio.h>

int greedy(int i);

int main(void)
{
    int i;
    //  error check using do function
    do
    {
        i = get_int("Change owed: ");
    }
    while (i < 0);
    printf("%i\n", greedy(i));
}

//  greedy function takes input and count coins variable.
//  possible to code with modulus % and if else.
int greedy(int i)
{
    int coin;

    coin = 0;
    while (i >= 25)
    {
        coin++;
        i -= 25;
    }
    while (i >= 10)
    {
        coin++;
        i -= 10;
    }
    while (i >= 5)
    {
        coin++;
        i -= 5;
    }
    while (i >= 1)
    {
        coin++;
        i -= 1;
    }
    return coin;
}
