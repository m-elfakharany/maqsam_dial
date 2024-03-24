from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # This method will be called when the 'Call' button is clicked
    def action_call_maqsam(self):
        self.ensure_one()
        if not self.mobile:
            raise UserError('No phone number is set for this contact.')

        phone_number = self.mobile  # assuming E.164 format

        # Here you would construct the URL to initiate the Maqsam auto-dial call
        maqsam_url = f"https://portal.maqsam.com/phone/dialer#autodial={phone_number}"

        return {
            'type': 'ir.actions.act_url',
            'url': maqsam_url,
            'target': 'new',
        }
