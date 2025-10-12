#include <stdio.h>

struct Word {
    char word[50];
    int count;
};

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    char *inputFile = argv[1];
    char stopFile[] = "stop_words.txt";

    /* --- Open and load stop words (lowercased) --- */
    FILE *f1 = fopen(stopFile, "r");
    if (f1 == NULL) {
        printf("Error: could not open stop words file.\n");
        return 1;
    }

    char stopWords[500][20];
    int stopTotal = 0;
    int c;
    int s_pos = 0;

    while ((c = fgetc(f1)) != EOF) {
        if (c == ',' || c == '\n') {
            if (s_pos > 0 && stopTotal < 500) {
                stopWords[stopTotal][s_pos] = '\0';
                stopTotal++;
                s_pos = 0;
            } else {
                /* consecutive delimiters -> skip */
                s_pos = 0;
            }
        } else {
            /* convert to lowercase if uppercase */
            if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
            /* store character if space in buffer */
            if (s_pos < 19) {
                stopWords[stopTotal][s_pos++] = (char)c;
            }
            /* else truncate */
        }
    }
    /* flush last stop word if file did not end with delimiter */
    if (s_pos > 0 && stopTotal < 500) {
        stopWords[stopTotal][s_pos] = '\0';
        stopTotal++;
        s_pos = 0;
    }
    fclose(f1);

    /* --- Read input file and build frequency list --- */
    FILE *f2 = fopen(inputFile, "r");
    if (f2 == NULL) {
        printf("Error: could not open input file.\n");
        return 1;
    }

    struct Word words[10000];
    int totalWords = 0;
    char current[50];
    int pos = 0;

    while ((c = fgetc(f2)) != EOF) {
        /* Lowercase uppercase letters */
        if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';

        /* If letter, accumulate */
        if (c >= 'a' && c <= 'z') {
            if (pos < 49) current[pos++] = (char)c;
        }
        /* Non-letter -> boundary */
        else {
            if (pos >= 2) { /* require length >= 2 to avoid single-letter tokens like 's' */
                current[pos] = '\0';

                /* check stop words (linear search) */
                int isStop = 0;
                for (int si = 0; si < stopTotal; si++) {
                    int k = 0;
                    int match = 1;
                    while (stopWords[si][k] != '\0' || current[k] != '\0') {
                        char a = stopWords[si][k];
                        char b = current[k];
                        if (a != b) {
                            match = 0;
                            break;
                        }
                        k++;
                    }
                    if (match) { isStop = 1; break; }
                }

                if (!isStop) {
                    /* find existing word */
                    int found = 0;
                    for (int wi = 0; wi < totalWords; wi++) {
                        int k = 0;
                        int match = 1;
                        while (words[wi].word[k] != '\0' || current[k] != '\0') {
                            char a = words[wi].word[k];
                            char b = current[k];
                            if (a != b) { match = 0; break; }
                            k++;
                        }
                        if (match) { words[wi].count++; found = 1; break; }
                    }

                    if (!found && totalWords < 10000) {
                        int k;
                        for (k = 0; current[k] != '\0'; k++) words[totalWords].word[k] = current[k];
                        words[totalWords].word[k] = '\0';
                        words[totalWords].count = 1;
                        totalWords++;
                    }
                }
            }
            /* reset current buffer */
            pos = 0;
        }
    }

    /* Handle last word at EOF (if file ended with a letter sequence) */
    if (pos >= 2) {
        current[pos] = '\0';

        int isStop = 0;
        for (int si = 0; si < stopTotal; si++) {
            int k = 0;
            int match = 1;
            while (stopWords[si][k] != '\0' || current[k] != '\0') {
                char a = stopWords[si][k];
                char b = current[k];
                if (a != b) { match = 0; break; }
                k++;
            }
            if (match) { isStop = 1; break; }
        }

        if (!isStop) {
            int found = 0;
            for (int wi = 0; wi < totalWords; wi++) {
                int k = 0;
                int match = 1;
                while (words[wi].word[k] != '\0' || current[k] != '\0') {
                    char a = words[wi].word[k];
                    char b = current[k];
                    if (a != b) { match = 0; break; }
                    k++;
                }
                if (match) { words[wi].count++; found = 1; break; }
            }
            if (!found && totalWords < 10000) {
                int k;
                for (k = 0; current[k] != '\0'; k++) words[totalWords].word[k] = current[k];
                words[totalWords].word[k] = '\0';
                words[totalWords].count = 1;
                totalWords++;
            }
        }
    }

    fclose(f2);

    /* --- Sort by frequency (descending) --- */
    for (int i = 0; i < totalWords - 1; i++) {
        for (int j = i + 1; j < totalWords; j++) {
            if (words[j].count > words[i].count) {
                struct Word tmp = words[i];
                words[i] = words[j];
                words[j] = tmp;
            }
        }
    }

    /* --- Print top 25 --- */
    int limit = totalWords < 25 ? totalWords : 25;
    for (int i = 0; i < limit; i++) {
        printf("%s  -  %d\n", words[i].word, words[i].count);
    }

    return 0;
}
