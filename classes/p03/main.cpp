#include <iostream>
#include <cmath>
#include <functional>
#include <utility>

double f1(double x, double y){
    return 2*pow(x,2) - x*y - 5*x + 1;
}

double f2(double x, double y){
    return x + 3* log(x) - pow(y,2);
}

double df1x(double x, double y){
    return -y + 4*x -5;
}

double df2y(double x, double y){
    return -2*y;
}

double df1y(double x, double y){
    return -x;
}

double df2x(double x, double y){
    return 3/x + 1;
}

double g1(double x, double y){
    return sqrt((x*y + 5*x -1)/2);
}

double g2(double x, double y){
    return sqrt(x+3*log(x));
}

std::pair<double,double> picard_peano(std::function<double(double, double)> g1,
              std::function<double(double, double)> g2,
              double x0, double y0){
    int count = 0;
    double error = pow(10,-6);
    double prev_x = x0, prev_y = y0;
    double x, y;
    for (; ; count++){
        x = g1(prev_x,prev_y);
        y = g2(prev_x,prev_y); //gauss-seider would be g2(x,prev_y);
        if (std::abs(x - prev_x) <= error && std::abs(y - prev_y) <= error) break;
        else{
            prev_x = x;
            prev_y = y;
        }
    }
    std::cout << count << " iterations\n";
    return std::make_pair(x,y);
}

std::pair<double,double> newton(std::function<double(double, double)> f1,
                                                     std::function<double(double, double)> f2,
                                                     std::function<double(double, double)> df1x,
                                                     std::function<double(double, double)> df1y,
                                                     std::function<double(double, double)> df2x,
                                                     std::function<double(double, double)> df2y,
                                                     double x0, double y0){
    int count = 0;
    double error = pow(10,-6);
    double prev_x = x0, prev_y = y0;
    double x, y;
    for (; ; count++){ //same as newton, but use new x to calculate y
        x = prev_x  - ((f1(prev_x,prev_y)*df2y(prev_x,prev_y) - f2(prev_x,prev_y)*df1y(prev_x,prev_y)) /
                       (df1x(prev_x,prev_y)*df2y(prev_x,prev_y) - df2x(prev_x,prev_y) * df1y(prev_x,prev_y)));
        y = prev_y  - (((f2(prev_x,prev_y)*df1x(prev_x,prev_y) - f1(prev_x,prev_y)*df2x(x,prev_y)) /
                        (df1x(prev_x,prev_y)*df2y(prev_x,prev_y) - df2x(prev_x,prev_y) * df1y(x,prev_y))));
        if (std::abs(x - prev_x) <= error && std::abs(y - prev_y) <= error) break;
        else{
            prev_x = x;
            prev_y = y;
        }
    }
    std::cout << count << " iterations\n";
    return std::make_pair(x,y);
}

int main() {
    std::pair<double,double> zeros_newton;
    std::pair<double,double> zeros_picard;
    zeros_newton = newton(f1,f2,df1x,df1y,df2x,df2y,4,4);
    std::cout << zeros_newton.first << " " << zeros_newton.second << "\n\n";

    zeros_picard = picard_peano(g1,g2,4,4);
    std::cout << zeros_picard.first << " " << zeros_picard.second << "\n";
}
