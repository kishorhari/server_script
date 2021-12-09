frappe.response['args']=(frappe.request.args)
frappe.response["args"]=(frappe.form_dict)

doctype = frappe.response['args']['doctype']
email = frappe.response['args']['email']
# frappe.log_error(email, doctype)
unsubscribe_email = frappe.db.get_value(doctype, {'email': email}, ['name'])
frappe.db.set_value(doctype, unsubscribe_email, {
    'unsubscribed': 1
})
frappe.response['message']= "Success"


# API call in cient scirpt

 frappe.call({
    method: "unsubscribe_service_from_lead",
    args: {
        doctype: "Email Group Member",
        email: cur_frm.doc.email_id
    },
    callback: function(resp) {
        if (resp) {
            // unsubscribe_service_from_lead
            frappe.set_route("List", "Lead");

        }
    }
})
