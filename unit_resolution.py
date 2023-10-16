'''
@Author:EricBi
@Purpose: For Calculation verifications
'''

def unit_resolution(clauses):
    unit_clauses = []
    while True:
        new_unit_clauses = [clause[0] for clause in clauses if len(clause) == 1]
        if not new_unit_clauses:
            break
        unit_clauses.extend(new_unit_clauses)
        for unit in new_unit_clauses:
            clauses = [clause for clause in clauses if unit not in clause]
            clauses = [list(filter(lambda x: x != -unit, clause)) for clause in clauses]
    return list(unit_clauses)

def condition(delta,I):
    conditioned_kb = []
    for clause in delta:
        # If the clause contains a literal in I, it's already satisfied
        if any(lit in I for lit in clause):
            continue

        # If clause contains negation of a literal in I, remove it from clause 
        # -> If lit did not cover a clause, the clause still remains unknown, still the remain clausecontributing to the logic output; in other words, if clause includes one of the I, it always be true 
        conditioned_clause = [lit for lit in clause if -lit not in I]
        
        # If clause becomes empty, we have a contradiction
        if not conditioned_clause:
            return []  # Return empty KB if contradiction is reached
        conditioned_kb.append(conditioned_clause)
    return conditioned_kb

# Improvement :
#    Char to Num, allowing input letters 


input = [
    [-1,-2],[2,3],[-3,4],[3]
]
output = unit_resolution(input)
print(output)
print(condition(input,output))

