# Copyright (c) 2026, Eammon Kiprotich and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Member(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data
		full_name: DF.Data
		outstanding_debt: DF.ReadOnly
		phone: DF.Data
	# end: auto-generated types

	def validate(self):
		debt = int(self.outstanding_debt)

		if debt < 0:
			frappe.throw("Outstanding debt cannot be negative")

		if debt > 500:
			frappe.throw("Outstanding debt cannot exceed KES 500")
