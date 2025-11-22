import numpy as np
import matplotlib.pyplot as plt

def testRuleset(a,b,limit):
    result = np.zeros((limit))
    for num in range(limit):
        outcome = evaluate(a,b,num+1)
        if outcome <= -1:
            return outcome
        result[num] = outcome
    return np.exp(np.log(result).mean())

def evaluate(a,b,num):
    iters = 0
    reached = []
    cursor = int(num)
    
    while iters < 10000 and cursor not in reached:
        reached.append(cursor)
        if cursor%2 == 0:
            cursor = cursor//2
        else:
            cursor = cursor*a+b
            
        if cursor >= 9999000000000:
            return -2
        iters += 1
    if cursor in reached:
        return iters
        
    return -1


def drawGrid(grid):
    FS = 10
    B = grid.shape[0]
    L = grid.shape[1]
    
    results_T = grid+2 #np.flip(np.transpose(grid), axis=0)
    results_H = np.flip(np.power(results_T, 0.3), axis=0)
    results_H /= np.amax(results_H)
    
    fig, ax = plt.subplots()
    im = ax.imshow(results_H)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(range(L), labels=range(L), ha="center", rotation_mode="anchor", fontsize=FS)
    ax.set_yticks(range(B), labels=range(B-1,-1,-1), ha="right", fontsize=FS)
    plt.xlabel("And then add", fontsize=FS, va="center")
    plt.ylabel("Multiply by", fontsize=FS, va="center")

    # Loop over data dimensions and create text annotations.
    for i in range(B):
        for j in range(L):
            val = results_T[i, j]-2
            c = "k"
            
            stri = f"{val:.3g}"
            if val == -2:
                #c = "w"
                stri = "ER"
            if val == -1:
                #c = "w"
                stri = "LR"
            
            text = ax.text(j, B-1-i, stri, ha="center", va="center", color=c, fontsize=FS)

    ax.set_title("Collatz-like average max growth", fontsize=FS)
    
    fig.tight_layout()
    
    plt.show()



limit = 1000000

A = 36
B = 71

grid = np.zeros((A, B))
for a in range(A):
    for b in range(B):
        grid[a,b] = testRuleset(a, b, limit)
    print(f"Done with {a} of {A}")
        
drawGrid(grid)
        