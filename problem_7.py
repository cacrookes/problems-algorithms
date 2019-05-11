#!/usr/bin/env python3


class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path):
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, path_part, handler=None):
        self.children[path_part] = RouteTrieNode(handler)


class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.root = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.root.insert(self.split_path(path), handler)

    def lookup(self, path):
        handler = self.root.find(self.split_path(path))
        if handler:
            return handler
        return self.not_found_handler

    def split_path(self, path):
        return [part for part in path.split('/') if part != '']


def run_tests():
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler'
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler'
    print(router.lookup("/home/about/me"))  # should print 'not found handler'


if __name__ == '__main__':
    run_tests()
