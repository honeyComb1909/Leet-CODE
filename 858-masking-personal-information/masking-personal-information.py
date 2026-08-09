class Solution:
    def maskPII(self, s):
        if '@' in s:
            # Email
            s = s.lower()

            name, domain = s.split('@')

            return name[0] + "*****" + name[-1] + "@" + domain

        else:
            # Phone number
            digits = ''.join(ch for ch in s if ch.isdigit())

            local = "***-***-" + digits[-4:]

            if len(digits) == 10:
                return local

            country = len(digits) - 10

            return "+" + "*" * country + "-" + local