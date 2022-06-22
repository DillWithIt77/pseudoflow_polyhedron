import time
import random
import numpy as np
import network as net
import math

from polyhedron import Polyhedron
from steepest_ascent import steepest_descent_augmentation_scheme as sdac


def main(A,B,b,d,c,x_feasible, results_dir='results',
         max_time=300, sd_method='dual_simplex', reset=False):
    
    print('Building polyhedron...')
    P = Polyhedron(B, d, A, b, c)
    
    print('Finding feasible solution...')
    # x_feasible = P.find_feasible_solution(verbose=False)
    print(x_feasible)
    print('Building gurobi model for simplex...')
    P.build_gurobi_model(c=c)
    P.set_solution(x_feasible)
    
    print('\nSolving with simplex method...')
    lp_result = P.solve_lp(verbose=False, record_objs=True)
    print('\nSolution using simplex method:')
    print(lp_result)
    
    print('\nSolving with steepest descent...')
    sd_result = sdac(P, x_feasible, c=c, method=sd_method, max_time=max_time, reset=reset)
    print('\nSolution using steepest-descent augmentation: ')
    print(sd_result)


if __name__ == "__main__":   
    #node arc incidence matrix
    M = 100

    ####typical steffen example####
    # A = np.array([[1,-1,0,0],[1,0,-1,0],[0,1,-1,0],[0,1,0,-1],[0,0,1,-1],[-1,0,0,1]]).transpose()
    # #flow balance and arc cap values (x arcs, s^+ arcs, s^- arcs)
    # b=np.array([0,0,0,0]).transpose()
    # d=np.array([0,0,0,0,0,0,2,4,3,1,5, math.inf,0,0,0,0,0,0,0,0]).transpose()
    # # d=np.array([0,0,0,0,0,0,100,100,1,100,100, math.inf,0,0,0,0,0,0,0,0]).transpose()
    # c = np.array([0,0,0,0,0,-1,M,M,M,M,M,M,M,M]).transpose()
    # feasible = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # A = net.add_slack_arcs(A)
    # B = net.construct_B(6,4,'True')

    ####second example####
    A = np.array([[1,-1,0,0,0,0],[1,0,0,-1,0,0],[0,1,-1,0,0,0],[0,1,0,-1,0,0],[0,0,1,0,-1,0],[0,0,1,0,0,-1],[0,0,-1,1,0,0],[0,0,0,1,-1,0],[0,0,0,0,1,-1],[-1,0,0,0,0,1]]).transpose()
    #flow balance and arc cap values (x arcs, s^+ arcs, s^- arcs)
    b=np.array([0,0,0,0,0,0]).transpose()
    d=np.array([0,0,0,0,0,0,0,0,0,0,6,6,3,7,2,4,1,2,4, math.inf,0,0,0,0,0,0,0,0,0,0,0,0]).transpose()
    c = np.array([0,0,0,0,0,0,0,0,0,-1,M,M,M,M,M,M,M,M,M,M,M,M]).transpose()
    feasible = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    A = net.add_slack_arcs(A)
    B = net.construct_B(10,6,'True')

    
    main(A,B,b,d,c,feasible,'results', 300, 'dual_simplex', 'False')