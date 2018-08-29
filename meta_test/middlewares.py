from scrapy import signals

class DownloaderMiddleware(object):

    @classmethod
    def process_request(self, request, spider):

        print("----------------------------------DOWNLOADERMIDDLEWARE > PROCESS_REQUEST----------------------------------")
        # item = request.meta['item']
        # print('----------------------------------DOWNLOADERMIDDLEWARE > PROCESS_REQUEST > PRINT ITEM: %s ----------------------------------' % item['main_url'])
        return None

    def process_response(self, request, response, spider):

        print("----------------------------------DOWNLOADERMIDDLEWARE > PROCESS_RESPONSE----------------------------------")
        return response


