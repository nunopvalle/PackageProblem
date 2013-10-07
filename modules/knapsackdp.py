# Routines for Knapsack Problem (CodeEval)

from util import*;

class KnapsackProblem:
    """ Instance of a Knapsack Problem """
    
    def __init__(self, bag_capacity, ids, weights, costs):
        # Data Inputs
        self.capacity = bag_capacity;
        self.set_ids = ids;
        self.weight_per_id = weights;
        self.cost_per_id = costs;

        # Auxiliary structures
        self.value_subproblems = dict();
        self.flag_subproblems = dict();     # 0 not added, 1 added item

    def solve(self):
        '''Solve the Knapsack Problem using Dynamic Programming'''

        last_item_id = -1;
        for item_id in self.set_ids:
            self.value_subproblems[item_id] = dict();
            for sub_capacity in range(self.capacity+1):
                self.sub_problem(self, item_id, sub_capacity, last_item_id);
            last_item_id = item_id;

    def sub_problem(self, item_id, sub_capacity, last_item_id):
        ''' Solve sub-problem with all the items until item_id and
        sub_capacity.
        '''
        
        cost = self.cost_per_id[item_id];
        weight = self.weight_per_id[item_id];
        sub_solution_value = 0;
        added = False;

        # In case it is not the first item
        if(last_item_id != -1):
            
            #Retrieve value of Fr-1(lambda)
            potential_solution1 = self.value_subproblems[last_item_id][sub_capacity];
            #Retrieve value of Fr-1(lambda)  
            potential_solution2 = 0;
            if sub_capacity - weight > 0:
                potential_solution2 = cost + \
                                      self.value_subproblems[last_item_id][sub_capacity - weight];
            if (potential_solution1 > potential_solution2):
                sub_solution_value = potential_solution1;
            else:
                sub_solution_value = potential_solution2;
                added = True;

        # If first item and weight fits the capacity
        elif weight >= sub_capacity:
            sub_solution_value = cost;
            added = True;

        #Note: In case weight < sub_capacity and it is the first item
        # the solution value is     0.

        self.value_subproblems[item_id][sub_capacity] = sub_solution_value;
        self.flag_subproblems[item_id][sub_capacity] = 1 if added else 0;
            
    def get_result(self):
        ''' Retrieve the solution to the problem'''

        result = list();
        current_capacity = self.capacity;
        iterator = Reverse(self.set_ids);
        while True:
            try:
                item_id = iterator.next();
            except StopIteration:
                break;
            if(self.flag_subproblems[item_id][current_capacity] == 1):
                result.append(item_id);
                current_capacity -= self.weight_per_id[item_id];
        return result;
            
            

