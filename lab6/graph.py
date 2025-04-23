def get_incident_matrix_from_adjacency_structure(
        adjacency_structure: dict[str, list[str]]
) -> dict[str, dict[tuple[str, str], int]]:
    incident_matrix = {}
    arcs: list[tuple[str, str]] = []

    for vertex1, vertices in adjacency_structure.items():
        for vertex2 in vertices:
            arcs.append((vertex1, vertex2))

    for vertex1, vertices in adjacency_structure.items():
        incidents: dict[tuple[str, str], int] = {
            arc: 0 for arc in arcs
        }
        for vertex2 in vertices:
            incidents[(vertex1, vertex2)] = 1
        incident_matrix[vertex1] = incidents

    for incidents in incident_matrix.values():
        for vertex1, vertex2 in incidents:
            incident_matrix[vertex2][(vertex1, vertex2)] = -1

    return incident_matrix


def get_adjacency_structure_from_incident_matrix(
        incident_matrix: dict[str, dict[tuple[str, str], int]]
) -> dict[str, list[str]]:
    adjacency_structure = {
        vertex: [] for vertex in incident_matrix
    }

    for incidents in incident_matrix.values():
        for (vertex1, vertex2), incident in incidents.items():
            if incident == 1:
                adjacency_structure[vertex1].append(vertex2)

    return adjacency_structure


if __name__ == '__main__':
    from pprint import pprint

    adj_struct = {
        'a': ['b', 'e', 'f'],
        'b': ['c'],
        'c': [],
        'd': ['c', 'g'],
        'e': ['d', 'f'],
        'f': ['d', 'g'],
        'g': ['c']
    }
    pprint(adj_struct)
    inc_matrix = get_incident_matrix_from_adjacency_structure(adj_struct)
    pprint(inc_matrix)
    adj_struct = get_adjacency_structure_from_incident_matrix(inc_matrix)
    pprint(adj_struct)
