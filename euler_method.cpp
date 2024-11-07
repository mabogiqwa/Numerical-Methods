//Euler method
#include <iostream>
#include <cmath>

double f_t_y(double t_i, double w_i);
//This formula is normally given as y'

int main()
{
    double stepSize = 0.5, nextWValue;
    double a = 0, b = 1, w_0 = 0, t_0 = 0;
    double numberOfSteps = (b - a)/stepSize;

    int iter = 1;
    do
    {
      nextWValue = w_0 + stepSize*f_t_y(t_0, w_0);

      w_0 = nextWValue;
      std::cout << w_0 << std::endl;
      t_0 = t_0 + stepSize*iter;
      iter = iter + 1;
    } while (iter <= numberOfSteps);


    return 0;
}

double f_t_y(double t_i, double w_i)
{
    return (t_i*exp(3*t_i) - 2*w_i);
}
