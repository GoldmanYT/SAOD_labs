from math import inf
from random import randint


def get_costs(n: int) -> list[list[int]]:
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r = randint(1, 9)
            a[i][j] = r
            a[j][i] = r
    return a


def print_costs(costs: list[list[int]]):
    n = len(costs)
    output_strings: list[str] = ['\t' + '\t'.join(f'[{i}]' for i in range(n))]
    for node in range(n):
        string = f'[{node}]\t' + '\t'.join(str(costs[node][i]) for i in range(n))
        output_strings.append(string)
    print('\n'.join(output_strings))


def branch_and_bound(costs: list[list[int]]):
    min_cost = inf
    cost = 0
    cur_node = 0
    s: list[list[int]] = []
    k = 0
    # while k >= 0:
    #     while s[k] and cost < min_cost:
    #         pass
    #     k -= 1
    #     cost -= costs[cur_node]


def greedy(costs: list[list[int]]):
    start_node = 0
    cur_node = start_node
    cost = 0
    solution: list[int] = []
    n = len(costs)

    for _ in range(n - 1):
        next_node = min(
            [node for node in range(n)
             if node not in solution and node not in (cur_node, start_node)],
            key=lambda node: costs[cur_node][node]
        )
        cost += costs[cur_node][next_node]
        solution.append(next_node)
        cur_node = next_node

    solution.insert(0, start_node)
    cost += costs[cur_node][start_node]
    solution.append(start_node)

    print(f'cost: {cost}')
    print('solution:', ' - '.join(map(str, solution)))


def main():
    n = 10
    costs = get_costs(n)

    print_costs(costs)
    branch_and_bound(costs)
    greedy(costs)


if __name__ == '__main__':
    main()
