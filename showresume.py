from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

import sys, string

from xml.etree.ElementTree import *
from xml.etree.ElementTree import tostring

class MainPage(webapp.RequestHandler):
    def get(self):
      tree = ElementTree()
      node = tree.parse(open("myresume.xml"))
      personname = node.find('.//PersonName/FormattedName').text
      street = node.find('.//ContactMethod/PostalAddress/DeliveryAddress').text
      cty = node.find('.//ContactMethod/PostalAddress/Municipality').text
      st = node.find('.//ContactMethod/PostalAddress/Region').text
      zip = node.find('.//ContactMethod/PostalAddress/PostalCode').text
      cellnum = node.find('.//ContactMethod/Telephone/Office').text
      officenum = node.find('.//ContactMethod/Telephone/Cell').text
      emailaddress = node.find('.//ContactMethod/InternetEmailAddress').text
      execsum = node.find('.//ExecutiveSummary').text
      obj = node.find('.//Objective').text
      
      employers = []
      for e in node.findall('.//EmploymentHistory/EmployerOrg'):
		employment = {}
		employment['organization'] = e.findtext('EmployerOrgName')
		employment['orgdomname'] = e.findtext('InternetDomainName')
		employment['startdt'] = e.findtext('PositionHistory/StartDate/YearMonth')
		employment['enddt'] = e.findtext('PositionHistory/EndDate/YearMonth')
		employment['title'] = e.findtext('PositionHistory/Title')
		employment['description'] = e.findall('PositionHistory/Description')
		employers.append(employment)
      
      school = []
      for s in node.findall('.//EducationHistory/SchoolOrInstitution'):
      		education = {}
      		education['sch'] = s.findtext('School/SchoolName')
      		education['schoolwebsite'] = s.findtext('School/InternetDomainName')
      		education['degree'] = s.findtext('Degree/DegreeName')
      		education['degreedate'] = s.findtext('Degree/DegreeDate/YearMonth')
      		school.append(education)
        
      references = []

      template_values = {
         'person': personname,
         'streetaddress': street,
         'city': cty,
         'state': st,
         'zipcode': zip,
         'office': officenum,
         'cell':cellnum,
         'email':emailaddress,
         'execsummary': execsum,
         'objective': obj,
         'employers': employers,
         'school': school,
      }
      
      path = os.path.join(os.path.dirname(__file__), 'index.html')
      self.response.out.write(template.render(path, template_values))
      
application = webapp.WSGIApplication([('/', MainPage)],debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
