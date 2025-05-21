#DOM
import xml.dom.minidom
from datetime import datetime

start_dom= datetime.now()

DOMTree=xml.dom.minidom.parse("go_obo.xml")
root = DOMTree.documentElement
terms = root.getElementsByTagName("term")
dic = {"biological_process": {"id": "", "name": "", "count": 0},
       "molecular_function": {"id": "", "name": "", "count": 0}, 
       "cellular_component": {"id": "", "name": "", "count": 0}}

for term in terms:
    id_tag = term.getElementsByTagName("id")
    term_id = id_tag[0].firstChild.nodeValue if id_tag else ""

    name_tag = term.getElementsByTagName("name")
    term_name = name_tag[0].firstChild.nodeValue if name_tag else ""

    namespace_tag = term.getElementsByTagName("namespace")
    namespace = namespace_tag[0].firstChild.nodeValue if namespace_tag else ""

    is_a_tags = term.getElementsByTagName("is_a")
    is_a_count = len(is_a_tags)

    if namespace in dic:
        if is_a_count > dic[namespace]["count"]:
            dic[namespace] = {"id": term_id,"name": term_name,"count": is_a_count}

print("DOM Results")
for key in dic:
    print(f"{key}: {dic[key]['id']} <{dic[key]['name']}>, {dic[key]['count']} parent terms")
end_dom = datetime.now()
time_dom = end_dom-start_dom
print("DOM running time:", time_dom)

#SAX
import xml.sax
from datetime import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.term_id = ""
        self.term_name = ""
        self.namespace = ""
        self.is_a_count = 0
        self.name_buffer = ""

        self.result = {"biological_process": {"id": "", "name": "", "count": 0},"molecular_function": {"id": "", "name": "", "count": 0},"cellular_component": {"id": "", "name": "", "count": 0}}

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if self.current_tag == "is_a":
            self.is_a_count += 1
        if tag == "term":
            self.term_id = ""
            self.term_name = ""
            self.namespace = ""
            self.is_a_count = 0
            self.name_buffer = ""

    def endElement(self, tag):
        if tag == "name":
            self.term_name = self.name_buffer.strip()
        elif tag == "term":
            if self.namespace in self.result:
                if self.is_a_count > self.result[self.namespace]["count"]:
                    self.result[self.namespace] = {"id": self.term_id,"name": self.term_name,"count": self.is_a_count}
    
    def characters(self, content):
        if self.current_tag == "id":
            self.term_id += content.strip()
        elif self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag=="name":
            self.name_buffer += content  # accumulate name
        
start_sax = datetime.now()
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml") 
end_sax = datetime.now()
time_sax = end_sax - start_sax

print("SAX Results")
for key in handler.result:
    print(f"{key}: {handler.result[key]['id']} <{handler.result[key]['name']}>, {handler.result[key]['count']} parent terms")
print("SAX running time:", time_sax)

#SAX is faster
if time_sax < time_dom:
    print("SAX is faster")
elif time_sax > time_dom:
    print("DOM is faster")
else:
    print("equal")