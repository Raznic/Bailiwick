HOSTNAME_REGEX = r"^[a-z0-9]+(-[a-z0-9]+)*$"
# Regex obtained from O'Reilly Regular Expressions Cookbook
# https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
FQDN_REGEX = r"^((?=[a-z0-9-]{1,63}\.)[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}$"
