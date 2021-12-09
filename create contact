frappe.response['args']=(frappe.request.args)

firstName = frappe.response['args']['customer_name']
emailId = frappe.response['args']['email_id']
phone = frappe.response['args']['phone']
name = frappe.response['args']['name']

insertContact = frappe.get_doc({
        "doctype": "Contact",
        "first_name":firstName,
        #"user":emailId,
        "phone_no":phone,
        "email_id":emailId
    }).insert()

#insertContact.submit()

childEmailInsert = insertContact.append('email_ids', {
    'email_id': emailId,
    'is_primary': True
}).insert()

childPhoneInsert = insertContact.append('phone_nos', {
    'phone': phone,
    'is_primary_phone': True,
    "is_primary_mobile_no": True
}).insert()

childLinksInsert = insertContact.append('links', {
    'link_doctype': "Customer",
    'link_name': name,
    "link_title": firstName
}).insert()

frappe.response['message'] = phone
#frappe.msgprint("hii",phone)
#ignore_permissions=True
# todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
# todo.insert(ignore_permissions=True)
# todo.submit()


#insertContact.insert(ignore_permissions=True)
insertContact.save()
