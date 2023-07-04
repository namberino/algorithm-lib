#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define POPSIZE 20
#define GAIA "ABC"

// Calc factorial num
int calcFact(int num)
{
    int i=num;

    while(--num)
        i*=num;
    return(i);
}

// Compare two organisms return 1 if equal 0 if not
int orgcmp(char *a, char *b, int len)
{
    int i,eq=0;

    for(i=0;i<len;i++,a++,b++)
        if(*a!=*b)
            return(0);
    return(1);
}

// Check an org versus the list of stored ones
// return 1 if the org is in the list
checkOrg(char *org, int ssize, char *found, int unique)
{
    int diff=0,i;

    if(unique==0) // None added yet
        return(0);
    
    for(i=0;i<unique && !diff;i++,found+=ssize) 
    {
        diff|=orgcmp(org,found,ssize);
    }
    return(diff);
}

// Copy org
orgcpy(char *dest, char *src, int ssize)
{
    int i;

    for(i=0;i<ssize;i++)
        dest[i]=src[i];
}

// Add unique orgs in population to the found list
// Use a hash if you have big strings
int addToFound(char **population, int popsize, int ssize, char *found, int unique)
{
    int org;
    // For each org in population
    for(org=0;org<popsize;org++,population++) 
    {
        if(!checkOrg(*population,ssize,found,unique)) 
        { //if not found yet
            orgcpy(found+ssize*unique,*population,ssize);
            printf("%s\n",*population); // Output
            unique++;
        }
    }
    return(unique);
}

// simple mutation - Randomly swap two characters
mutate(char *population, int ssize)
{
    char c;
    int i,c1,c2;

    // Swap two characters
    c1=random() % ssize;
    c2=random() % ssize;
    c=population[c1];
    population[c1]=population[c2];
    population[c2]=c;
}

// Generate permations genetically
perms(char **population, int popsize, int ssize)
{
    int permsTotal,unique=0,i,g;
    char *found,*saved;

    // Calc Total perms
    permsTotal=calcFact(ssize);
    // Create found pool
    saved=found=malloc((ssize)*sizeof(char)*permsTotal);
    memset(found,0,(ssize)*sizeof(char)*permsTotal);

    // Until we find all perms
    while(unique<permsTotal) 
    {
        // Add uniques to list
        unique=addToFound(population,popsize,ssize,found,unique);
        // Mutate population
        for(i=0;i<popsize;i++)
        mutate(population[i],ssize);
    }
    free(saved);
}

// Init PRNG
// Allocate and initialize first generation
// Call the perm generator
main(int argc, char *argv[])
{
    char string[]=GAIA;
    char *population[POPSIZE];
    int i;

    srandom(time(NULL)); // /dev/random better
    for(i=0;i<POPSIZE;i++) 
    {
        population[i]=malloc(sizeof(string));
        strcpy(population[i],string);
    }

    perms(population,POPSIZE,strlen(string));
}
