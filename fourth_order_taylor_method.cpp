#include <iostream>
#include <cmath>

double f(double t, double w);

double f_derivative(double t, double w);

double f_second_derivative(double t, double w);

double f_third_derivative(double t, double w);

double compute_fourth_order_taylor(double t, double w, double stepSize);

int main()
{
    double w_0 = 1, t_0 = 0;
    double nextWValue, stepSize = 0.5;

    int iter = 1;
    do
    {
      std::cout << "Approximate value of w_i: " << nextWValue << std::endl;
      nextWValue = w_0 + stepSize*compute_fourth_order_taylor(t_0, w_0,stepSize);
      t_0 = t_0 + stepSize;
      w_0 = nextWValue;

      iter = iter + 1;
    } while (iter <= 3);


    return 0;
}

double f(double t, double w)
{
   return exp(t - w);
}

double f_derivative(double t, double w)
{
   return (1 - exp(t - w))*exp(t - w);
}

double f_second_derivative(double t, double w)
{
   return exp(t - 3*w)*(2*exp(2*t) + exp(2*w) - 3*exp(t + w));
}

double f_third_derivative(double t, double w)
{
   return exp(t - 4*w)*(-6*exp(3*t) + exp(3*w) + 12*exp(2*t + w) - 7*exp(t + 2*w));
}

double compute_fourth_order_taylor(double t, double w, double stepSize)
{
    return (f(t, w) + (stepSize/2.00)*f_derivative(t, w) + (pow(stepSize, 2)/6.00)*f_second_derivative(t, w) + (pow(stepSize, 3)/24.00)*f_third_derivative(t, w));
}
