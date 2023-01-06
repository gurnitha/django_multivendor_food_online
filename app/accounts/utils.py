# app/accounts/utils.py

def detectUser(user):
    if user.role == 1:
        # redirectUrl = 'vendorDashboard' # this did not work because of i used: app/accounts
        redirectUrl = '../vendorDashboard' # this works
        return redirectUrl
    elif user.role == 2:
        # redirectUrl = 'custDashboard'   # this did not work because of i used: app/accounts
        redirectUrl = '../custDashboard'  # this works
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl