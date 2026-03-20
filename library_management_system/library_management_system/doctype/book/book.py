# Copyright (c) 2026, Eammon Kiprotich and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Book(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		author: DF.Data
		available_quantity: DF.Data
		isbn: DF.Data | None
		title: DF.Data
		total_quantity: DF.Data
	# end: auto-generated types

	pass
