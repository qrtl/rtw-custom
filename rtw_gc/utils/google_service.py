# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.google_account.models.google_service import TIMEOUT
from odoo.addons.google_calendar.utils.google_calendar import GoogleCalendarService


class GoogleCalendarService(GoogleCalendarService):
    def get_events(self, sync_token=None, token=None, timeout=TIMEOUT):
        print("test")
        # if xxx:
        #     (custom logic here)
        return super().get_events(sync_token=sync_token, token=token, timeout=timeout)

    def insert(self, values, token=None, timeout=TIMEOUT):
        print("test")
        return super().insert(token=token, timeout=timeout)

