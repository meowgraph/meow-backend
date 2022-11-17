import json
from Library.settings import graph
from py2neo import Node, Relationship


def importEntity(entitiesFile):
    fin = open(entitiesFile, encoding='utf-8', mode='r')
    for line in fin.readlines():
        line = json.loads(line)
        if line['id'] % 100 == 0:
            print("entity: " + str(line['id']))
        entities = line['entities']
        for entity in entities:
            nodes = graph.nodes.match(entity['type'], name=entity['name'])
            if len(nodes) != 0:
                node = nodes.first()
                if line['ISBN'] not in node['belong']:
                    node['belong'].append(line['ISBN'])
                    tx = graph.begin()
                    tx.push(node)
                    graph.commit(tx)
            else:
                node = Node(entity['type'], name=entity['name'])
                node['belong'] = [line['ISBN']]
                graph.create(node)

    fin.close()


def importRelations(relationsFile):
    fin = open(relationsFile, encoding='utf-8', mode='r')
    for line in fin.readlines():
        line = json.loads(line)
        if line['id'] % 100 == 0:
            print("relation: " + str(line['id']))

        h = graph.nodes.match(line['h']['type'], name=line['h']['name']).first()
        t = graph.nodes.match(line['t']['type'], name=line['t']['name']).first()

        relations = graph.relationships.match((h, t), r_type=line['relation'])
        if len(relations) != 0:
            relation = relations.first()
            if line['ISBN'] not in relation['belong']:
                relation['belong'].append(line['ISBN'])
                tx = graph.begin()
                tx.push(relation)
                graph.commit(tx)
        else:
            relation = Relationship(h, line['relation'], t)
            relation['belong'] = [line['ISBN']]
            graph.create(relation)


def createNeo4j(entitiesFile, relationsFile):
    importEntity(entitiesFile)
    importRelations(relationsFile)
