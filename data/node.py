"""
 <node id="4532714102" visible="true" version="6" changeset="81641150" timestamp="2020-03-01T11:15:40Z" user="Gilmar Ferreira" uid="2336678" lat="-19.9246276" lon="-43.9524513">
  <tag k="addr:city" v="Belo Horizonte"/>
  <tag k="addr:housenumber" v="747"/>
  <tag k="addr:postcode" v="30180-090"/>
  <tag k="addr:street" v="Rua Paracatu"/>
  <tag k="addr:suburb" v="Barro Preto"/>
  <tag k="name" v="Momento Super Nosso"/>
  <tag k="name:pt" v="Momento Super Nosso"/>
  <tag k="opening_hours" v="Mo-Sa 07:00-21:00; PH,Su 08:00-14:00; PH"/>
  <tag k="phone" v="+55 31 3359-3265"/>
  <tag k="shop" v="supermarket"/>
  <tag k="website" v="http://momentosupernosso.com.br"/>
 </node>

"""

class Node:
    def __init__(self, id, lat, lon, tags):
        self.id = id
        self.lat = lat
        self.lon = lon

        self.tags = tags