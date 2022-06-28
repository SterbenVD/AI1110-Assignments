#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(){
    FILE *fp = fopen("./uni.dat","r+");
    for(int i = 0; i < 1000000; i++){
        double var = ((double)rand())/RAND_MAX;
        fprintf(fp, "%lf\n",var);
    }
    fclose(fp);
    return 0;
}