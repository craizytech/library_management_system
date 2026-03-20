# Copyright (c) 2026, Eammon Kiprotich and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import date_diff, nowdate


class Transaction(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		book: DF.Link
		fee: DF.Currency
		issue_date: DF.Date
		member: DF.Link
		name: DF.Int | None
		return_date: DF.Date | None
		status: DF.Literal["Issued", "Returned"]
	# end: auto-generated types

	def validate(self):
		if self.status == "Issued":
			self.handle_issue()

		elif self.status == "Returned":
			self.handle_return

	# Handling issuing
	def handle_issue(self):
		book = frappe.get_doc("Book", self.book)
		member = frappe.get_doc("Member", self.member)

		if book.available_quantity <= 0:
			frappe.throw(_("Book is out of stock"))

		if member.outstanding_debt > 500:
			frappe.throw(_("Member has exceeded the max allowed debt."))

		if not self.issue_date:
			self.issue_date = nowdate()

	# handling return
	def handle_return(self):
		if not self.return_date:
			self.return_date = nowdate

		if not self.issue_date:
			frappe.throw(_("Issue date is required before return"))

		days = date_diff(self.return_date, self.issue_date)
		self.fee = max(days, 0) * 10

	# handle changes in stock
	def on_submit(self):
		if self.status == "Issued":
			self.apply_issue()

		if self.status == "Returned":
			self.apply_return()

	def apply_issue(self):
		book = frappe.get_doc("Book", self.book)
		book.available_quantity -= 1
		book.save()

	def apply_return(self):
		book = frappe.get_doc("Book", self.book)
		member = frappe.get_doc("Member", self.member)

		book.available_quantity += 1
		book.save()

		member.outstanding_debt += self.fee
		member.save()
