from collections import deque


class SubtreeMover:
    """
    The SubtreeMover class is responsible for handling the movement of a node and its connected subtree
    within a graph. It provides functionality to move a selected node along with all its connected child nodes,
    maintaining the relative positions within the subtree.
    """

    def __init__(self):
        pass

    def move_selected_node_subtree(self, node_to_move, dx, dy):
        """
        Moves a selected node and its entire subtree by a specified offset.

        :param: node_to_move: The node to be moved, along with its subtree.
        :param: dx: The change in the x-coordinate for the movement.
        :param: dy: The change in the y-coordinate for the movement.

        This method updates the position of the specified node and recursively moves all connected nodes (its subtree),
        ensuring the entire structure is translated by the same offset.
        """
        if node_to_move is None:
            return

        # Update the position of the selected node
        node_to_move.x += dx
        node_to_move.y += dy

        # Use a queue to process child nodes
        queue = deque()
        queue.extend(node_to_move.get_connected_nodes().values())

        # Use a set to track visited nodes
        visited_nodes = {node_to_move}

        while queue:
            child = queue.popleft()
            # Check if Child Node has been visited
            if child not in visited_nodes:
                # Move the child node
                child.x += dx
                child.y += dy
                # Add the child node's children to the queue for processing
                queue.extend(child.get_connected_nodes().values())
                # Add the child node to the set of visited nodes
                visited_nodes.add(child)
