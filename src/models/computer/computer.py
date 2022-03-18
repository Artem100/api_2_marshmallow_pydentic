class Computer:

    def __init__(self, id, status, activated_at, expiration_at, host_v4, host_v6):
        self.id = id
        self.status = status
        self.activated_at = activated_at
        self.expiration_at = expiration_at
        self.host_v4 = host_v4
        self.host_v6 = host_v6