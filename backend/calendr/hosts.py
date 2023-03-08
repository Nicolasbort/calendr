from django_hosts import host, patterns

# Routes "api.calendr..." or "calendr..." subdomains to api.urls
# and "management.calendr..." subdomain to management.urls
host_patterns = patterns(
    "",
    host(r"(|api)", "api.urls", name="api"),
    host(r"management", "management.urls", name="management"),
)
