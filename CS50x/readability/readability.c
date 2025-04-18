// Problem Set 2: Readability
// This program uses Coleman-Liau index, to calculate the reading level of the text input.
//  This program uses one main and two functions, in main, I gathered the get_string; then churn the index using colemanlia();
//  lastly, using grading() to determine the print result. The limitation of my program is that it captures ".", "!", "?" char as
//  sentences.
//   Future version can implement more checks to capture conditions such as "U.S.A." as a word instead of three sentences.

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int colemanliau(char *str);
void grading(int res);

int main(void)
{
    char *str;

    str = get_string("Text: ");
    grading(colemanliau(str));

    return 0;
}

int colemanliau(char *str)
{
    float letter;
    float word;
    float sentence;
    float index;
    float al;
    float as;

    letter = 0;
    word = 0;
    sentence = 0;

    if (*str == '\0' || *str == ' ' || *str == '.')
        return 0;

    while (*str != '\0')
    {
        *str = tolower(*str);
        if ((*str >= 'a' && *str <= 'z') || (*str >= '0' && *str <= '9'))
        {
            letter++;
        }
        else if (*str == ' ')
        {
            word++;
        }
        else if ((*str == '.' || *str == '!' || *str == '?'))
        {
            sentence++;
            if (*(str + 1) == '\0')
                word++;
        }
        str++;
    }
    al = letter / word * 100;
    as = sentence / word * 100;
    index = 0.0588 * al - 0.296 * as - 15.8;
    // checks
    // printf("Letter = %f\nWord = %f\nSentence = %f\nal = %f\nas = %f\nindex = %f\n", letter, word, sentence, al, as, index);
    return (round(index));
}

void grading(int res)
{
    if (res >= 2 && res <= 15)
        printf("Grade %d\n", res);
    else if (res <= 1)
        printf("Before Grade 1\n");
    else
        printf("Grade 16+\n");
}
