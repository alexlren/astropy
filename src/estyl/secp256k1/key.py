import hashlib
import hmac

from estyl.secp256k1.ecc import GROUP_G, ORDER_N, Point


class Signature:
    def __init__(self, r: int, s: int):
        self.r = r
        self.s = s


class PrivateKey:
    def __init__(self, secret: int):
        self.secret = secret

    def _calculate_k(self, z: int) -> int:
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > ORDER_N:
            z -= ORDER_N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < ORDER_N:
                return candidate
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()

    def sign(self, z: int) -> Signature:
        k = self._calculate_k(z)
        R = k * GROUP_G
        r = R.x.val
        k_inv = pow(k, ORDER_N - 2, ORDER_N)

        s = (z + r * self.secret) * k_inv % ORDER_N
        return Signature(r, s)


class PublicKey:
    def __init__(self, pub: Point):
        self.pub = pub

    @classmethod
    def from_secret(cls, secret: int) -> 'PublicKey':
        return cls(secret * GROUP_G)

    def verify(self, z: int, sig: Signature) -> bool:
        s_inv = pow(sig.s, ORDER_N - 2, ORDER_N)
        u = z * s_inv % ORDER_N
        v = sig.r * s_inv % ORDER_N
        R = u * GROUP_G + v * self.pub
        return sig.r == R.x.val
