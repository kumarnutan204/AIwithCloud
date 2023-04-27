#include <iostream>
#include <cstdlib>
#include <cstring>
#define MAX_STACK_SIZE 100
using namespace std;
struct Block {
    char *name;
    int x, y;
};
Block *table[5][5];
Block *stack[MAX_STACK_SIZE];
int stack_top = 0;
void initialize() {
    int i, j;
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            table[i][j] = NULL;
        }
    }
}
Block *create_block(char *name, int x, int y) {
    Block *block = new Block;
    block->name = strdup(name);
    block->x = x;
    block->y = y;
    table[x][y] = block;
    return block;
}
void print_table() {
    int i, j;
    for (i = 0; i < 5; i++) {
        cout << "|";
        for (j = 0; j < 5; j++) {
            if (table[i][j] == NULL) {
                cout << "   |";
            } else {
                cout << " " << table[i][j]->name << " |";
            }
        }
        cout << endl;
    }
}
void push(Block *block) {
    if (stack_top == MAX_STACK_SIZE) {
        cerr << "Error: Stack overflow" << endl;
        exit(1);
    }
    stack[stack_top++] = block;
}
Block *pop() {
    if (stack_top == 0) {
        cerr << "Error: Stack underflow" << endl;
        exit(1);
    }
    return stack[--stack_top];
}
void move(Block *block, int x, int y) {
    int i, j;
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            if (table[i][j] == block) {
                table[i][j] = NULL;
            }
        }
    }
    block->x = x;
    block->y = y;
    table[x][y] = block;
    push(block);
}
void undo() {
    Block *block = pop();
    table[block->x][block->y] = NULL;
    block->x = -1;
    block->y = -1;
}
int main() {
    initialize();
    Block *a = create_block("A", 0, 0);
    Block *b = create_block("B", 0, 1);
    Block *c = create_block("C", 0, 2);
    Block *d = create_block("D", 0, 3);
    Block *e = create_block("E", 0, 4);
    print_table();
    cout << "Move A from (0, 0) to (2, 2)" << endl;
    move(a, 2, 2);
    print_table();
    cout << "Move C from (0, 2) to (1, 4)" << endl;
    move(c, 1, 4);
    print_table();
    cout << "Undo the last move" << endl;
    undo();
    print_table();
    return 0;
}