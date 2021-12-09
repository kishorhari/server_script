lead_details = frappe.db.get_list('Lead',
        filters={
            'name': doc.party_name
        },
        fields=['primary_mobile', 'email_id', 'lead_name']
    )
    
frappe.log_error(lead_details[0].email_id)
email = lead_details[0].email_id
phone = lead_details[0].primary_mobile
name = lead_details[0].lead_name

user = frappe.db.get_value("User", {"name": email})
if not user:
    doc = frappe.get_doc({
        'doctype': 'User',
        "name": email,
		"email": email,
		"enabled": 1,
		"first_name": first_name or email,
		"user_type": "Website User",
		"send_welcome_email": 0
    })
    doc.insert(ignore_permissions=True)
    roles = ["Customer"]
    doc.add_roles(*roles)
    doc.save(ignore_permissions=True)
else:
    frappe.msgprint("User Already Exists")
    
