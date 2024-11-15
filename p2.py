def get_orbs(potion, recipes, memo):
    # If potion is already computed, return its value from memo
    if potion in memo:
        return memo[potion]
    
    # If potion is an item (i.e., not in recipes), it requires 0 orbs to brew
    if potion not in recipes:
        memo[potion] = 0
        return 0
    
    # Initialize the minimum orbs to a large number
    min_orbs = float('inf')
    
    # Iterate through all possible ways to make the potion
    for ingredients in recipes[potion]:
        total_orbs = sum(get_orbs(ingredient, recipes, memo) for ingredient in ingredients) + len(ingredients) - 1
        min_orbs = min(min_orbs, total_orbs)
    
    # Save the result in memo for future reference
    memo[potion] = min_orbs
    return min_orbs

def main():
    # Read the number of recipes
    N = int(input().strip())
    
    # Dictionary to store recipes: potion -> list of ingredients
    recipes = {}
    
    # Read the recipes
    for _ in range(N):
        line = input().strip()
        potion, recipe = line.split('=')
        ingredients = recipe.split('+')
        
        # If potion already exists, append this new way to make it
        if potion in recipes:
            recipes[potion].append(ingredients)
        else:
            recipes[potion] = [ingredients]
    
    # Read the target potion
    target_potion = input().strip()
    
    # Memoization dictionary
    memo = {}
    
    # Compute and print the result
    print(get_orbs(target_potion, recipes, memo), end="")

if __name__ == "__main__":
    main()
