include "globals.mzn";

int: n = 9; % number of cells
set of int: DOMAIN = 1..n; % defining the domain of the variables
array [DOMAIN, DOMAIN] of var DOMAIN: cell; % defining the cells

array[DOMAIN, DOMAIN] of int: pre; % input matrix where are definined the assigned values

% constraints on the rows and the columns
constraint forall(i in DOMAIN)
    (alldifferent([cell[i, j] | j in DOMAIN]));
    
constraint forall(i in DOMAIN)
    (alldifferent([cell[j, i] | j in DOMAIN]));
    
set of int: D1 = 1..3;
set of int: D2 = 4..6;
set of int: D3 = 7..9;

% constraints on the cells
constraint alldifferent([cell[i,j] | i in D1, j in D1]);
constraint alldifferent([cell[i,j] | i in D1, j in D2]);
constraint alldifferent([cell[i,j] | i in D1, j in D3]);
constraint alldifferent([cell[i,j] | i in D2, j in D1]);
constraint alldifferent([cell[i,j] | i in D2, j in D2]);
constraint alldifferent([cell[i,j] | i in D2, j in D3]);
constraint alldifferent([cell[i,j] | i in D3, j in D1]);
constraint alldifferent([cell[i,j] | i in D3, j in D2]);
constraint alldifferent([cell[i,j] | i in D3, j in D3]);

% constraint on the pre defined values
constraint forall(i,j in DOMAIN) (
    if pre[i,j] != 0 
      then cell[i,j] = pre[i,j]
    else true
    endif
);
        
solve satisfy;