#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
// Function declaration
//double **createMat(int m, int n);
//void readMat(double **p, int m, int n);
//void print(double **p, int m, int n);
//double **loadtxt(char *str, int m, int n);
//double linalg_norm(double **a, int m);
//double **linalg_sub(double **a, double **b, int m, int n);
//double **linalg_inv(double **mat, int m);
//double **matmul(double **a, double **b, int m, int n, int p);
//double **transpose(double **a, int m, int n);
void uni_gen(char *str, int len);
void gau_gen(char *str, int len);
double gen_mean(char *str);
double gen_var(char *str, double mean);
void tri_gen(char *str, int len);
// End function declaration

void uni_gen(char *str, int len){
    FILE *fp = fopen(str,"w");
    for(int i = 0; i < len; i++){
        double var = ((double)rand())/RAND_MAX;
        fprintf(fp, "%lf\n",var);
    }
    fclose(fp); 
}

void gau_gen(char *str, int len){
    FILE *fp = fopen(str,"w");
    for(int i = 0; i < len; i++){
        srand(i);
        double x=0;
        for(int j = 0; j<12;j++){
            double U = ((double)rand())/RAND_MAX;
            x+= U;
        }
        fprintf(fp, "%lf\n",x-6.0);
    }
    fclose(fp);
}

double gen_mean(char *str)
{
    FILE *fp = fopen(str,"r");
    double sum = 0,num=0;
    int total_num=0;
    while(fscanf(fp,"%lf",&num)!=-1){
        sum+=num;
        total_num++;
        if(feof(fp)){break;};
    }
    fclose(fp);
    double mean = sum/total_num;
    return mean;
}

double gen_var(char *str, double mean){
    FILE *fp = fopen("./uni.dat","r");
    double sum = 0, num =0;
    int total_num=0;
    while(fscanf(fp,"%lf",&num)!=-1){
        sum+= pow((num - mean),2.0);
        total_num++;
        if(feof(fp)){break;};
    }
    fclose(fp);
    double var = sum / total_num;
    return var;
}

void tri_gen(char *str, int len){
    FILE *fp = fopen(str,"w");
    for(int i = 0; i < len; i++){
        srand(i);
        double x=0;
        for(int j = 0; j<2;j++){
            double U = ((double)rand())/RAND_MAX;
            x+= U;
        }
        fprintf(fp, "%lf\n",x);
    }
    fclose(fp);
}