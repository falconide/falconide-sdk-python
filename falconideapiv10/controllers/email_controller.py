# -*- coding: utf-8 -*-

"""
    falconideapiv10.controllers.email_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
import requests
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration

class EmailController(BaseController):

    """A Controller to access Endpoints in the falconideapiv10 API."""


    def get_falconapi_web_send_rest(self,
                                    api_key,
                                    mfrom,
                                    subject,
                                    content,
                                    recipients,
                                    fromname=None,
                                    replytoid=None,
                                    footer=True,
                                    template=None,
                                    attachmentid=None,
                                    clicktrack=True,
                                    opentrack=True,
                                    bcc=None,
                                    att_name=None,
                                    x_apiheader=None,
                                    tags=None):
        """Does a GET request to /falconapi/web.send.rest.

        `Sending Mails` – This API is used for sending emails. Falconide
        supports REST as well JSON formats for the input

        Args:
            api_key (string): Your API Key
            mfrom (string): From email address
            subject (string): Subject of the Email
            content (string): Email body in html (to use attributes to display
                dynamic values such as name, account number, etc. for ex. [%
                NAME %] for ATT_NAME , [% AGE %] for ATT_AGE etc.)
            recipients (string): Email addresses for recipients (multiple
                values allowed)
            fromname (string, optional): Email Sender name
            replytoid (string, optional): Reply to email address
            footer (bool, optional): Set '0' or '1' in order to include footer
                or not
            template (int, optional): Email template ID
            attachmentid (string, optional): specify uploaded attachments id
                (Multiple attachments are allowed)
            clicktrack (bool, optional): set ‘0’ or ‘1’ in-order to disable or
                enable the click-track
            opentrack (bool, optional): set open-track value to ‘0’ or ‘1’
                in-order to disable or enable
            bcc (string, optional): Email address for bcc
            att_name (string, optional): Specify attributes followed by ATT_
                for recipient to personalized email for ex. ATT_NAME for name,
                ATT_AGE for age etc. (Multiple attributes are allowed)
            x_apiheader (string, optional): Your defined unique identifier
            tags (string, optional): To relate each message. Useful for
                reports.

        Returns:
            void: Response from the API. Success | Failure

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/falconapi/web.send.rest'
        _query_parameters = {
            'api_key': api_key,
            'from': mfrom,
            'subject': subject,
            'content': content,
            'recipients': recipients,
            'fromname': fromname,
            'replytoid': replytoid,
            'footer': footer,
            'template': template,
            'attachmentid': attachmentid,
            'clicktrack': clicktrack,
            'opentrack': opentrack,
            'bcc': bcc,
            'ATT_NAME': att_name,
            'X-APIHEADER': x_apiheader,
            'tags': tags
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        req = requests.get(_query_url,headers={"content-type":"application/json; charset=utf-8"})		
        return req.json()

    def create_falconapi_web_send_json(self,
                                       data):
        """Does a POST request to /falconapi/web.send.json.

        `Sending Mails` – This API is used for sending emails. Pepipost
        supports REST as well JSON formats for the input. This is JSON API.

        Args:
            data (Emailv1): Data in JSON format

        Returns:
            void: Response from the API. Success | Failure

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/falconapi/web.send.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        headers = {"content-type":"application/x-www-form-urlencoded; charset=utf-8"}		
        body = {'data':APIHelper.json_serialize(data)}
        # Prepare and execute request
        req = requests.post(_query_url,data=body)   
        return req.json()

