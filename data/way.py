"""

 <way id="278275959" visible="true" version="11" changeset="108273538" timestamp="2021-07-19T20:04:17Z" user="hayduke1275" uid="12854712">
  <nd ref="2826717002"/>
  <nd ref="2962508633"/>
  <nd ref="2843901101"/>
  <tag k="highway" v="secondary"/>
  <tag k="lanes" v="2"/>
  <tag k="name" v="Avenida Barbacena"/>
  <tag k="oneway" v="yes"/>
  <tag k="sidewalk" v="right"/>
  <tag k="surface" v="asphalt"/>
 </way>

"""

class Way:
    def __init__(self, id, nds, postes, tags):
        self.id = id
        
        self.nds = nds
        self.postes = postes
        self.tags = tags