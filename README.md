# problem description
Assume that we have chess board with some soldier in fix positions the problem is to locate queen somehow maximize the defined fitness function.

Fitness function:
- if two queens threaten each other -2 points are given
- each soldier has a specific point if it is threatened by a queen the point would be given

# algorithm
I used genetic algorithm to solve this problem with this config
- population size of 100
- parent size of 20
- spontaneous mutation with 0.05 probablity
- single point crossover with 0.8 probablity


# run
first of all install openCV
```
    pip install -r opencv-python
```
then run the main.py
```
    python3 main.py
```
here it is the result for a 18*18 board which red cells are soldier and green cells are queens.

![Position_Notation](https://github.com/Mehrdadghassabi/altered_nqueen_problem/assets/53050138/4dff08ac-fe40-4d82-8e86-93e81ff45707)
