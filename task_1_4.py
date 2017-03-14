def check_domain_name(email):
    """
    Function that check subdomain valid.
    """
    if email == None:
        return None

    dname = email.split("@")[1]

    if len(dname) < 2 or dname.endswith("."):
        return None

    for subd in dname.split("."):
        if len(subd) < 2:
            return None

    return email


def check_email_name(email):
    """
    Function that check email name valid.
    """
    if email == None:
        return None

    name = email.split("@")[0]

    if len(name) == 0:
        return None
    
    for ch in name:
        if not ch.isalnum() and ch != "_":
            return None

    return email


def filer_func(emails):
    """
    The main filtered function that validate email.
    """
    email_list = list(filter(lambda em: "@" in em, emails))
    email_list = list(map(check_email_name, email_list))
    email_list = list(map(check_domain_name, email_list))

    email_list = list(filter(lambda el: el != None, email_list))
    email_list.sort()

    return email_list


if __name__ == "__main__":

    emails = ['abc@gmail.com.ua', '*@ank.com', '_ny@us.gov.us', 'z@b.kk', 'gg-gg.com']

    result_list = filer_func(emails)
    print("\nValid email list: \n{0}".format(result_list))