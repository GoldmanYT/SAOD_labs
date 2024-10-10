from tree import Tree, Node


def main():
    tree = Tree(
        Node(
            'a',
            Node(
                'b',
                Node(
                    'c',
                    Node('d')
                ),
                Node(
                    'e',
                    Node(
                        'f',
                        Node('g'),
                        Node(
                            'h',
                            Node('i')
                        )
                    ),
                    Node(
                        'j',
                        Node(
                            'k',
                            Node(
                                'l',
                                Node('m')
                            )
                        )
                    )
                )
            ),
            Node(
                'n',
                Node(
                    'o',
                    Node(
                        'p',
                        Node('q')
                    ),
                    Node('r')
                )
            )
        )
    )
    print(tree)


if __name__ == '__main__':
    main()