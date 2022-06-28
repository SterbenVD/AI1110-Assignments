#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(){
    FILE *fp = fopen("./gau.dat","r+");
    for(int i = 0; i < 1000000; i++){
        srand(i);
        double x=0;
        for(int j = 0; j<12;j++){
            double var = ((double)rand())/RAND_MAX;
            x+= var;
        }
        fprintf(fp, "%lf\n",x-6.0);
    }
    fclose(fp);
    return 0;
}