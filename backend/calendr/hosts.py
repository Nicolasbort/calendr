from django_hosts import host, patterns

# Routes "api.calendr..." or "calendr..." subdomains to api.urls
# and "admin.calendr..." subdomain to administration.urls
print("HOSTS\n")

host_patterns = patterns(
    "",
    host(r"(|api)", "api.urls", name="api"),
    host(r"admin", "administration.urls", name="administration"),
)
