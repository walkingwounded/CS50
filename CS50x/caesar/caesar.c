// Problem Set 2: Caesar

// Caesar is a simple dechiper code by inserting a constant digit, "Key", when running the program.
//  The program will then prompt a "plaintext" to be input.
//  The program will add the "Key" into the "plaintext" by shifting the ASCII alphabet forward.
//  I wrote a main() function with two other functions.
//  The main() function do a series of checks for proper inputs.
//  The only_digit() function returns true of false from the input.
//  The decode() function shift the ASCII forward and rotates the alphabet when it "z", meaning after "z", the next alphabet is "a",
//   instead of ASCII '123'.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void decode(char *s, int k);
bool only_digit(char *s);

int main(int argc, char **argv)
{
    int key;
    char *ptext;

    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!only_digit(argv[1]))
    {
        printf("Usage: ./caesar key (digit)\n");
        return 1;
    }

    key = atoi(argv[1]);
    if (key < 0)
    {
        printf("Usage: ./caesar key(constant)\n");
        return 1;
    }
    ptext = get_string("plaintext: ");
    decode(ptext, key);
    printf("ciphertext: %s\n", ptext);
    return 0;
}

// Decode the plaintext using the key
void decode(char *s, int k)
{
    int n;
    k = k % 26;

    while (*s != '\0')
    {
        n = 0;
        if (*s >= 97 && *s <= 122)
        {
            n = (*s + k);
            if (n > 122)
                *s = (n % 122) + 96;
            else
                *s = (*s + k);
            printf("%d\n", k);
            s++;
        }
        else if (*s >= 65 && *s <= 90)
        {
            *s = (*s + k);
            if (*s > 90)
                *s = (*s % 90) + 64;
            printf("%d, %d\n", k, s[0]);
            s++;
        }
        else
        {
            s++;
        }
    }
}

// Checks if char is a digit.
bool only_digit(char *s)
{
    while (*s != '\0')
    {
        if (!isdigit(*s))
            return false;
        s++;
    }
    return true;
}
