verify(String jwt){
  SignedJWT signedJWT = SignedJWT.parse(jwt);
  String[] jwtPart=jwt.split("\\.");
  String algo = "HMACSHA512";
  SecretKeySpec sk = new SecretKeySpec(clientSecret.getBytes(), algo);
  Mac mac = Mac.getInstance(algo);
  mac.init(sk);

  String signedContent = String.join(".",jwtPart[0],jwtPart[1]);
  mac.update(signedContent.getBytes());
  byte[] exp=mac.doFinal();

  return ConstantTimeUtils.areEqual(exp, signedJWT.getSignature().decode());
}
