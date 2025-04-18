#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define ALPHABET_LENGTH 26

// Function prototypes
int is_valid_key(char *key);
void encrypt_message(char *plaintext, char *key);

int main(int argc, char *argv[]) {
    // Ensure the user provided a key
    if (argc != 2) {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Validate the key
    char *key = argv[1];
    if (!is_valid_key(key)) {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }

    // Get the plaintext from the user
    char plaintext[256];
    printf("plaintext: ");
    if (fgets(plaintext, sizeof(plaintext), stdin) == NULL) {
        printf("Error reading plaintext.\n");
        return 1;
    }

    // Remove the newline character from fgets
    plaintext[strcspn(plaintext, "\n")] = '\0';

    // Encrypt the message
    printf("ciphertext: ");
    encrypt_message(plaintext, key);

    return 0;
}

// Check if the key is valid
int is_valid_key(char *key) {
    if (strlen(key) != ALPHABET_LENGTH) {
        return 0;
    }

    int seen[ALPHABET_LENGTH] = {0};
    for (int i = 0; i < ALPHABET_LENGTH; i++) {
        if (!isalpha(key[i])) {
            return 0;
        }
        int index = toupper(key[i]) - 'A';
        if (seen[index]) {
            return 0;
        }
        seen[index] = 1;
    }

    return 1;
}

// Encrypt the plaintext using the key
void encrypt_message(char *plaintext, char *key) {
    for (int i = 0; plaintext[i] != '\0'; i++) {
        char c = plaintext[i];
        if (isalpha(c)) {
            int is_lower = islower(c);
            char encrypted_char = is_lower ? tolower(key[c - 'a']) : toupper(key[c - 'A']);
            printf("%c", encrypted_char);
        } else {
            printf("%c", c);
        }
    }
    printf("\n");
}
