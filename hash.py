import importlib, MainExceptions, description
import zlib, hashlib
def mainloop(args):
	if args!=[]:
		hashtype = args[0]
		tohash = args[1]
		tohash = tohash.encode('utf-8')
		if hashtype in description.section_avalibale('hash', 'available'):
			if hashtype == 'sha1':
				obj = hashlib.sha1(tohash).hexdigest()
				return obj
			elif hashtype == 'shake_128':
				obj = hashlib.shake_128(tohash).hexdigest()
				return obj
			elif hashtype == 'sha384':
				obj = hashlib.sha384(tohash).hexdigest()
				return obj
			elif hashtype == 'blake2b':
				obj = hashlib.blake2b(tohash).hexdigest()
				return obj
			elif hashtype == 'blake2s':
				obj = hashlib.blake2s(tohash).hexdigest()
				return obj
			elif hashtype == 'sha3_224':
				obj = hashlib.sha3_224(tohash).hexdigest()
				return obj
			elif hashtype == 'sha224':
				obj = hashlib.sha224(tohash).hexdigest()
				return obj
			elif hashtype == 'sha3_256':
				obj = hashlib.sha3_256(tohash).hexdigest()
				return obj
			elif hashtype == 'sha3_384':
				obj = hashlib.sha3_384(tohash).hexdigest()
				return obj
			elif hashtype == 'sha512':
				obj = hashlib.sha512(tohash).hexdigest()
				return obj
			elif hashtype == 'shake_256':
				obj = hashlib.shake_256(tohash).hexdigest()
				return obj
			elif hashtype == 'sha3_512':
				obj = hashlib.sha3_512(tohash).hexdigest()
				return obj
			elif hashtype == 'sha256':
				obj = hashlib.sha256(tohash).hexdigest()
				return obj
			elif hashtype == 'md5':
				obj = hashlib.md5(tohash).hexdigest()
				return obj
			elif hashtype == 'crc32':
				obj = zlib.crc32(tohash)
				return obj
			elif hashtype == 'adler32':
				obj = zlib.adler32(tohash)
				return obj
		else: return 'Unknown hash!'
	else: raise MainExceptions.NoArgumentSet