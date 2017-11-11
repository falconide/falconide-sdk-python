# -*- coding: utf-8 -*-

"""
    falconideapiv10.models.settings

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class Settings(object):

    """Implementation of the 'settings' model.

    TODO: type model description here.

    Attributes:
        footer (bool): TODO: type description here.
        clicktrack (bool): TODO: type description here.
        opentrack (bool): TODO: type description here.
        unsubscribe (bool): TODO: type description here.
        bcc (string): TODO: type description here.
        attachmentid (string): TODO: type description here.
        template (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "footer" : "footer",
        "clicktrack" : "clicktrack",
        "opentrack" : "opentrack",
        "unsubscribe" : "unsubscribe",
        "bcc" : "bcc",
        "attachmentid" : "attachmentid",
        "template" : "template"
    }

    def __init__(self,
                 footer=True,
                 clicktrack=True,
                 opentrack=True,
                 unsubscribe=True,
                 bcc=None,
                 attachmentid=None,
                 template=None):
        """Constructor for the Settings class"""

        # Initialize members of the class
        self.footer = footer
        self.clicktrack = clicktrack
        self.opentrack = opentrack
        self.unsubscribe = unsubscribe
        self.bcc = bcc
        self.attachmentid = attachmentid
        self.template = template


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        footer = dictionary.get("footer") if dictionary.get("footer") else True
        clicktrack = dictionary.get("clicktrack") if dictionary.get("clicktrack") else True
        opentrack = dictionary.get("opentrack") if dictionary.get("opentrack") else True
        unsubscribe = dictionary.get("unsubscribe") if dictionary.get("unsubscribe") else True
        bcc = dictionary.get("bcc")
        attachmentid = dictionary.get("attachmentid")
        template = dictionary.get("template")

        # Return an object of this model
        return cls(footer,
                   clicktrack,
                   opentrack,
                   unsubscribe,
                   bcc,
                   attachmentid,
                   template)


