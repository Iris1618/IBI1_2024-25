import xml.sax
from datetime import datetime
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag=''
        self.current_namespace=''
        self.current_name=''
        self.is_a_count=0
        self.GO_terms={'molecular_function':{'term':'','count':0},
                       'biological_process':{'term':'','count':0},
                       'cellular_component':{'term':'','count':0},}
    def startElement(self,tag,attributes):
        self.current_tag=tag
        if tag=='term':
            self.current_namespace=''
            self.is_a_count=0
    def characters(self,content):
        if self.current_tag=='namespace':
            self.current_namespace=content
        elif self.current_tag=='names':
            self.current_names=content
        elif self.current_tag=='is_a':
            self.is_a_count+=1
    def endElement(self,tag):
        if tag=='term':
            if self.current_namespace in self.GO_terms:
                if self.is_a_count>self.GO_terms[self.current_namespace]['count']:
                    self.GO_terms[self.current_namespace]={'term':self.current_name,'count':self.is_a_count}
        self.current_tag = ""
start=datetime.now()
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=GOHandler()
parser.setContentHandler(Handler)
parser.parse("go_obo.xml")
print(Handler.GO_terms)
end=datetime.now()
time_of_SAX=end-start
print(time_of_SAX)