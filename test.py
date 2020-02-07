#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include <time.h>
#include <editline/readline.h>
#include <editline/history.h>

typedef struct command_args {
    struct command_args* next;
    char* arg;
} command_args_t;


void command_add_item(command_args_t, uint8_t);
void command_show_inventory(command_args_t, uint8_t);
void command_bye(command_args_t, uint8_t);

typedef void (*command_func_t)(command_args_t, uint8_t);


#define COMMAND_NUMBER 3
char* command_table[] = {
    "add",
    "inventory",
    "bye"
};

command_func_t command_func_table[] = {

    &command_add_item,
    &command_show_inventory,
    &command_bye
};

#define ADD_ARGS 4

#define WEAPON 0x0001
#define ARMOR  0x0002
#define MAGIC  0x0004
#define MISC   0x0008

typedef struct items {
    struct items*   next;
    char*           name;
    uint16_t        price;
    uint8_t         weight;
    uint8_t         type;
} items;

typedef struct player {
    uint16_t coins;
    uint8_t  health;
    items    i;
} player;

player hero;

items* inventory_current = &hero.i;
void add_item(char* name, uint16_t price, uint8_t weight, uint8_t type) {
    inventory_current->next = (items*)malloc(sizeof(items));
    inventory_current->next->name   = strdup(name);
    inventory_current->next->price  = price;
    inventory_current->next->weight = weight;
    inventory_current->next->type   = type;
    inventory_current->next->next   = NULL;

    inventory_current = inventory_current->next;

    return;
}

void command_add_item(command_args_t args, uint8_t argc) {
    if(argc < ADD_ARGS) {
        printf("[!] you're missing something\n");
        return;
    }

    printf("\tName: %s\n", args.arg);
    printf("\tPrice: %s",  args.next->arg);
    printf("\tWeight: %s", args.next->next->arg);
    printf("\tType: %s\n", args.next->next->next->arg);

    add_item(args.arg, atoi(args.next->arg), atoi(args.next->next->arg), atoi(args.next->next->next->arg));

    return;
}

void show_inventory() {
    items* current = &hero.i;
    for(; current; current = current->next) {
        printf("\tINVENTORY\n");
        printf("\t\tName: %s\n", current->name);
        printf("\t\tPrice: %d", current->price);
        printf("\t\t Weight: %d", current->weight);
        printf("\t\tType: %d\n", current->type);
    }

    return;
}

void command_show_inventory(command_args_t _args, uint8_t _argc) {
    show_inventory();
}

void command_bye(command_args_t _args, uint8_t _argc) {
    exit(0);
}


void process_input(char* input) {
        char* term;
        command_func_t command = NULL;
        command_args_t args;
        uint8_t argc;

        term = strtok(input, " ");

        for(size_t i = 0; i < COMMAND_NUMBER; i++) {
            if(strcmp(term ,command_table[i]) == 0) {
                command = command_func_table[i];
                break;
            }
        }

        if(!command) {
            printf("How should I know how to do that?\n");
            return;
        }

        args.next = malloc(sizeof(command_args_t));
        command_args_t* current = &args;
        for(argc = 0; term = strtok(NULL, " "); argc++) {
            current->next = malloc(sizeof(command_args_t));
            current->arg = term;
            current = current->next;
        }
        current->next = NULL;

        command(args, argc);
}

int main() {
    srand(time(NULL));

    hero.health   = 100;
    hero.coins    = 10;
    hero.i.name   = "Inventory";
    hero.i.weight = 0;
    hero.i.price  = 0;
    hero.i.type   = MISC;
    hero.i.next   = NULL;

    //add_item("Inventory", 0, 0, MISC);

    char* input;
    while(input = readline("> ")) {
        if(input == "") continue;
        add_history(input);
        process_input(input);
        free(input);
    }
}
