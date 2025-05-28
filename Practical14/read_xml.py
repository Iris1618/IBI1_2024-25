#DOM
import xml.dom.minidom
from datetime import datetime

start_dom= datetime.now()

DOMTree=xml.dom.minidom.parse("go_obo.xml")
root = DOMTree.documentElement
terms = root.getElementsByTagName("term")
dic = {"biological_process": {"max_count": 0, "terms": []},    # if more than one term has the max_count
    "molecular_function": {"max_count": 0, "terms": []},
    "cellular_component": {"max_count": 0, "terms": []}}


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
        max_count = dic[namespace]["max_count"]
        if is_a_count > max_count:
            dic[namespace]["max_count"] = is_a_count
            dic[namespace]["terms"] = [{"id": term_id,"name": term_name}]
        elif is_a_count==max_count:
            dic[namespace]["terms"].append({"id": term_id,"name": term_name})

print("DOM Results")
for key in dic:
    print(f"{key}:")
    for term in dic[key]["terms"]:
        print(f"  - {term['id']} <{term['name']}>")
    print(f"  Max is_a count: {dic[key]['max_count']}")

end_dom = datetime.now()
time_dom = end_dom-start_dom
print("DOM running time:", time_dom)

#SAX
import xml.sax
from datetime import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.term_name = ""
        self.namespace = ""
        self.is_a_count = 0
        self.name_buffer = ""
        self.term_id = ""

        self.result={}
        GO=["biological_process","molecular_function","cellular_component"]
        for i in GO:
            self.result[i] = {"max_count": 0,"terms": []}

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if self.current_tag == "is_a":
            self.is_a_count += 1
        if tag == "term":
            self.term_name = ""
            self.term_id = ""
            self.namespace = ""
            self.is_a_count = 0
            self.name_buffer = ""

    def endElement(self, tag):
        if tag == "name":
            self.term_name = self.name_buffer.strip()
        elif tag == "term":
            if self.namespace in self.result:
                current_max = self.result[self.namespace]["max_count"]
                current_terms = self.result[self.namespace]["terms"]
                if self.is_a_count > current_max:
                    self.result[self.namespace]["max_count"] = self.is_a_count
                    self.result[self.namespace]["terms"] = [{"id": self.term_id,"name": self.term_name}]
                elif self.is_a_count == current_max:
                    self.result[self.namespace]["terms"].append({"id": self.term_id,"name": self.term_name})
    
    def characters(self, content):
        if self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag=="name":
            self.name_buffer += content.strip()
        elif self.current_tag == "id":
            self.term_id += content.strip()
        
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
    print(f"{key}:")
    for term in handler.result[key]["terms"]:
        print(f"  - {term['id']} <{term['name']}>")
    print(f"  Max is_a count: {handler.result[key]['max_count']}")

print("SAX running time:", time_sax)

# SAX was faster in this run
if time_sax < time_dom:
    print("SAX is faster")
elif time_sax > time_dom:
    print("DOM is faster")
else:
    print("equal")