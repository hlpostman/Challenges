def get_permutations(nums: [int]) -> [[int]]:
    if not nums:
        return []
    return get_permutations_helper([], nums, [])

def get_permutations_helper(current_permutation: [int], decision_space: [int], solutions_array: [[int]]) -> [[int]]:
    for i in range(len(decision_space)):
        # Choose
        next_choice = decision_space[i]
        # print("decision space starts loop", i, "as", decision_space)
        current_permutation.append(next_choice)
        decision_space = decision_space[:i]+decision_space[i+1:]
        # print("post removal, decision space is", decision_space)
        # Construct
        get_permutations_helper(current_permutation, decision_space, solutions_array)
        if len(decision_space) == 0:
            # print("CURRENT PERMUTATION IS", current_permutation)
            solutions_array += [current_permutation.copy()]
        # Backtrack
        backtrack_item = current_permutation.pop()
        decision_space = decision_space[:i]+[backtrack_item]+decision_space[i:]
        # print("reconstructed, decision space is", decision_space)
    # print(solutions_array)
    return solutions_array


