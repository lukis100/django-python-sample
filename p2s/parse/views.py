from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Used to open url
import urllib 
# Used to parse
from xml.dom import minidom

from django.db.utils import IntegrityError

from models import HourlyIntegratedLMP, DayAheadLMP

def save(model, data):
  for record in data:
    model(name=record['name'], LMP=record['LMP'], MCC=record['MCC'], MLC=record['MLC']).save()

def parse(LMP_node_tag_name, dom):
  LMP_node = dom.getElementsByTagName(LMP_node_tag_name)[0]
  data = []
  for PricingNode in LMP_node.getElementsByTagName('PricingNode'):
    PricingNode_attribute_name = PricingNode.getAttribute('name')
    if PricingNode_attribute_name == u'MINN.HUB' or \
      PricingNode_attribute_name == u'MICHIGAN.HUB' or \
      PricingNode_attribute_name == u'INDIANA.HUB' or \
      PricingNode_attribute_name == u'ILLINOIS.HUB':
      data.append({
                 'name': PricingNode.getAttribute('name'),
                 'LMP': float(PricingNode.getAttribute('LMP')),
                 'MCC': float(PricingNode.getAttribute('MCC')),
                 'MLC': float(PricingNode.getAttribute('MLC'))
                 })
  return data

def home(request):
  if HourlyIntegratedLMP.objects.count()==0 and DayAheadLMP.objects.count()==0:
    return render_to_response('index.html')
  else:
    HILMP_records = HourlyIntegratedLMP.objects.all()
    DALMP_records = DayAheadLMP.objects.all()
  return render_to_response('index.html', {'HILMP_records': HILMP_records, 'DALMP_records': DALMP_records})
  
def ParseFeed(request):
  ### Parse URL
  url = 'https://www.midwestiso.org/ria/Consolidated.aspx?format=xml'
  dom = minidom.parse(urllib.urlopen(url))
  try:
    # Parse data
    HILMP_data = parse('HourlyIntegratedLMP', dom)
    DALMP_data = parse('DayAheadLMP', dom)
    # Save data
    save(HourlyIntegratedLMP, HILMP_data)
    save(DayAheadLMP, DALMP_data)
  except IntegrityError:
    pass
  
  return HttpResponseRedirect('/')