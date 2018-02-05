#include<stdio.h>

void dec(char *enc, int len) {

    char x = '\xff';

    for (int i = 0; i < len; i++) {
        int t = enc[i];
        enc[i] = enc[i] ^ x;
        x = t;
    }

    return;
}

int main(int argc, char **argv) {
    char enc[] = "\x84\xf4\x83\xe7\xb8\xcb\xa2\xcf\xbf\xd3\xb6\xe9\x8f\xfa\x94\xcb\xb3\xdc\xae\xf1\x83\xe6\x90\xf5\x87\xf4\x91\xe3\x9e\x00";

    dec(enc,0x1C);

    printf("Password: '%s'\n", enc);
}

