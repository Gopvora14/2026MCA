from passlib.context  import CryptContext

pwd_context = CryptContext (schemes=["bycrypt"], deprecated ="auto")

password = "Gop2004"

hashed = pwd_context.hash (password)

print ("original:" , password)
print ("hashed" , hashed)

print ("valid" , pwd_context.verify(password , hashed))