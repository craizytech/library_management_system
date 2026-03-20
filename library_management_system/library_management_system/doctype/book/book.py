# Copyright (c) 2026, Eammon Kiprotich and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Book(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		author: DF.Data
		available_quantity: DF.Int
		isbn: DF.Data | None
		title: DF.Data
		total_quantity: DF.Int
	# end: auto-generated types

	def validate(self):
		if not self.available_quantity:
			self.available_quantity = self.total_quantity

		available = int(self.available_quantity)
		total = int(self.total_quantity)

		if available > total:
			frappe.throw("Available quantity cannot exceed total quantity")
			
		if available < 0:
			frappe.throw("Available quantity cannot be negative")
