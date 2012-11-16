# coding: utf-8
from node import Node

from tests import _BaseErlangTestCase


class SimpleNodeTestCase(_BaseErlangTestCase):

    def test(self):
        node = Node('test', self.erl_node_secret, 9999)
        node.start()
        node.connect_node(self.erl_node_name)
        self.assertEqual(
            node.node_connections[self.erl_node_name].state,
            'connected'
        )
        self.assertTrue('test' in self.to_erl('erlang nodes [hidden]'))
        node.join(0.1)
