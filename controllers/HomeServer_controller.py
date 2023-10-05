from my_framework.my_http.base_controller import BaseController
from my_framework.my_http.http_data_types import HttpResponse
from dtos.message import Message

from wakeonlan import start_home_server
from config import STATUS_LINK, SHUTDOWN_LINK

import urequests

class HomeServerController(BaseController):
    def __init__(self):
        base_path="/HomeServer"
        super().__init__(base_path)
        
        self.methods_dict["post_shutdown"] += "/shutdown"
        self.methods_dict["post_start"] += "/start"
        self.methods_dict["get_status"] += "/status"

    def post_start(self, http_request):

        start_home_server()

        body = Message("Starting up!(magic package sent)")
        response = HttpResponse(200, {}, body)
        return response

    def post_shutdown(self, http_request):

        try:
            urequests.post(SHUTDOWN_LINK)
            body = Message("Shutting down!")
            response = HttpResponse(200, {}, body)
            return response
        except:
            body = Message("Server not responding!(Probably off)")
            response = HttpResponse(200, {}, body)
            return response
    
    def get_status(self, http_request):

        try:
            urequests.get(STATUS_LINK)
            body = Message("All ok!")
            response = HttpResponse(200, {}, body)
            return response
        except:
            body = Message("Server not responding!(Probably off)")
            response = HttpResponse(200, {}, body)
            return response