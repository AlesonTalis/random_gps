"""

 <relation id="12995015" visible="true" version="1" changeset="108274048" timestamp="2021-07-19T20:22:35Z" user="hayduke1275" uid="12854712">
  <member type="way" ref="965731249" role="from"/>
  <member type="way" ref="279160689" role="to"/>
  <member type="node" ref="4682305709" role="via"/>
  <tag k="restriction" v="no_left_turn"/>
  <tag k="type" v="restriction"/>
 </relation>

"""

class Member:
    def __init__(self, type, ref, role):
        self.type = type
        self.ref = ref
        self.role = role