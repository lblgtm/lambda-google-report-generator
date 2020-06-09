

import argparse
import sys


from apiclient import sample_tools
from oauth2client import client



class GoogleReport():

    def __init__(self):
        # Declare command-line flags.
        argparser = argparse.ArgumentParser(add_help=False)
        argparser.add_argument(
            '--report_id',
            help='The ID of the saved report to generate')
        arg = []
        arg.append(sys.argv[0])
        # Authenticate and construct service.
        self.service, flags = sample_tools.init(
        arg,'adsense', 'v1.4', __doc__, __file__, parents=[argparser],
        scope='https://www.googleapis.com/auth/adsense.readonly')

    def gen_report(self):
        result = self.service.accounts().reports().generate(
        accountId='cnet_newsletters_test', startDate='today-2m', endDate='today',
        metric=['PAGE_VIEWS', 'IMPRESSIONS', 'CLICKS','PAGE_VIEWS_RPM','IMPRESSIONS_RPM','EARNINGS'],
        dimension=['AD_CLIENT_ID', 'CUSTOM_CHANNEL_NAME','PLATFORM_TYPE_NAME','DATE',],filter='AD_CLIENT_ID==partner-web-search').execute()
        return result


    def generate(self,start_date,end_date):
        result = self.service.accounts().reports().generate(
        accountId='cnet_newsletters_test', startDate=start_date, endDate=end_date,
        metric=['PAGE_VIEWS', 'IMPRESSIONS', 'CLICKS','PAGE_VIEWS_RPM','IMPRESSIONS_RPM','EARNINGS'],
        dimension=['AD_CLIENT_ID', 'CUSTOM_CHANNEL_NAME','PLATFORM_TYPE_NAME','DATE']).execute()
        metrics = []
        for colms in result['rows']:
            metrics.append({
                        "ad_client_id":colms[0], 
                        "custom_chanel_name":colms[1], 
                        "platform_type_name":colms[2], 
                        "date":colms[3], 
                        "page_views":colms[4], 
                        "impressions":colms[5], 
                        "clicks":colms[6], 
                        "page_views_rpm":colms[7], 
                        "impressions_rpm":colms[8], 
                        "earnings":colms[9] 
                    })
        return metrics
