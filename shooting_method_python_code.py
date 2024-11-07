import math

# Constants
xinitial = 0.0
xfinal = 1.0
yinitial = 0.0
yfinal = 2.0
zinit1 = 1.9
zinit2 = 2.1
h = 0.2
tolerance = 1e-7
jmax = 10

# Functions for calculating fy and fz
def fy(x, y, z):
    return z  # y' = z

def fz(x, y, z):
    return 4*x*y + (x**2)*(2*x + 6 - z) - 2  # z' = 4xy + x^2(2x + 6 - z) - 2

# Function to perform the calculation using the modified Euler method
def calculate(zinitial):
    x = xinitial
    y = yinitial
    z = zinitial
    imax = round((xfinal - xinitial) / h)

    # Print the header
    print(f"{'x':12s} {'y':12s} {'z':12s}")

    # Iterate using the modified Euler method
    for i in range(1, imax + 1):
        fy0 = fy(x, y, z)
        yp = y + h * fy0
        fz0 = fz(x, y, z)
        zp = z + h * fz0
        x = x + h
        y = y + h * (fy0 + fy(x, yp, zp)) / 2
        z = z + h * (fz0 + fz(x, yp, zp)) / 2
        print(f"{x:12.6f} {y:12.6f} {z:12.6f}")

    yend = y
    print(f"Error in final y = {(yfinal - yend):12.6f}")
    return yend

# Function to print the exact solution
def print_exact():
    print(f"\nExact solution")
    print(f"{'x':12s} {'y':12s} {'z':12s}")
    imax = round((xfinal - xinitial) / h)
    
    for i in range(imax + 1):
        x = xinitial + i * h
        y = x**2 * (x**2 - 1) + 2 * x
        z = x * (4 * x**2 - 2) + 2
        print(f"{x:12.6f} {y:12.6f} {z:12.6f}")

# Main program to initialize values and run the calculation
def main():
    # Initialize the first and second estimates for z
    zi = [0] * jmax
    yf = [0] * jmax

    # Open the output file
    with open('apm3711.dat', 'w') as file:
        file.write("\n\n***** Question 2 *****\n")

        # Initial estimates for zi[1] and zi[2]
        zi[0] = zinit1
        yf[0] = calculate(zi[0])

        zi[1] = zinit2
        yf[1] = calculate(zi[1])

        j = 2
        while True:
            # Interpolate previous two values to find the next estimate for z
            zi[j] = zi[j - 2] + (zi[j - 1] - zi[j - 2]) * (yfinal - yf[j - 2]) / (yf[j - 1] - yf[j - 2])
            yf[j] = calculate(zi[j])
            j += 1

            if abs(yf[j - 1] - yfinal) < tolerance or j == jmax:
                break

        file.write(f"Number of iterations = {j}\n")
        
        # Print the exact solution
        print_exact()

# Run the main program
if __name__ == "__main__":
    main()
