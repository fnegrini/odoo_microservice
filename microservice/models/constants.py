
from odoo import models, fields, api, _

REQUEST_STATE = \
    [
        ('initial', _('Initial')),
        ('staggered', _('Staggered')),
        ('processed', _("Processed")),
        ('error', _("Error")),

    ]