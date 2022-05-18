class Solution:
    def numUniqueEmails(self, emails):
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unique_emails.add(local + "@" + domain)
        return len(unique_emails)
        