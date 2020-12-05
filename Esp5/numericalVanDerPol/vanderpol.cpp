#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <vector>

using namespace std;

#define NSTEPS 1000

/* 
RK4 and Euler integrators for the Van der Pol equation 
The Van der Pol equation can be transformed into 2 coupled first order ODE 
by defining the function u(t) = xdot(t) so that udot(t) = xdotdot(t)
*/

double udot(double t, double u, double x, double mu, double Vref);
double xdot(double t, double u);

int main(){

    // Output file
    ofstream outfile;
    outfile.open("./numerical.csv");

    // Measurements
    const double R0 = 1e6;
    const double RF = 10e3; // Feedback resistor
    const double R1 = 1e6;
    const double R2 = 100;
    const double R = 100e3;
    const double C = 10e-9;
    // Various useful parameters
    const double dt = 0.1;
    //const double ws = 1/R*C;
    const double ws = 1;
    const double r = R2/(R1+R2);
    const double Is = 5e-25;
    const double beta = 40.0;
    const double n = 1.5;
    const double chi = 0.5/(1+Is*beta*R0/n);
    const double csi = Is*R0*pow(beta, 3)/(3.0*pow(n, 3)*pow(chi, 4));
    //const double mu = ws*(RF/R0*chi - 2*r);
    const double mu = 0.6;
    const double Vref = sqrt((RF/R0*chi-2.0*r)/(3.0*RF/R0*csi));

    // Initial conditions
    double x = 2.5;
    cout << x << endl;
    double u = 0.0;
    double t = 0.0;
    
    // Euler integration
    /*outfile << "t,x" << endl; // Write column labels to file
    outfile << t << "," << x << endl;
    for (int n=0; n<NSTEPS; n++){
        x += xdot(t, u, mu, ws)*dt;
        u += udot(t, u)*dt;
        t += dt;
        outfile << t << "," << x << endl; // Write time and x to file
    }*/
    double k1u, k2u, k3u, k4u;
    double k1x, k2x, k3x, k4x;
    // RK4 integration
    outfile << "t,x,xdot" << endl;
    outfile << t << "," << x << "," << u << endl;
    for (int n=0; n<NSTEPS; n++){
        k1u = udot(t, u, x, mu, ws);
        k1x = xdot(t, u);
        k2u = udot(t+0.5*dt, u+0.5*k1u*dt, x+0.5*k1x*dt, mu, ws);
        k2x = xdot(t+0.5*dt, u+0.5*k1u*dt);
        k3u = udot(t+0.5*dt, u+0.5*k2u*dt, x+0.5*k2x*dt, mu, ws);
        k3x = xdot(t+0.5*dt, u+0.5*k2u*dt);
        k4u = udot(t+0.5*dt, u+k3u*dt, x+k3x*dt, mu, ws);
        k4x = xdot(t+0.5*dt, u*k3u*dt);
        u += dt/6 * (k1u + 2*k2u + 2*k3u + k4u);
        x += dt/6 * (k1x + 2*k2x + 2*k3x + k4x);
        t += dt;
        outfile << t << "," << x << "," << u << endl; // Write time and x to file
    }

    // Close output file
    outfile.close();

    return 0;

}

double udot(double t, double u, double x, double mu, double ws){
    return mu*(1 - pow(x,2))*u - pow(ws, 2)*x;
}
double xdot(double t, double u){
    return u;
}