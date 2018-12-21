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


String header=JSON.toJSONString(Collections.singletonMap("alg","HS256"));
String headerBase = new String(Base64.getEncoder().encode(header.getBytes()));
errCase(subject);
String payload=JSON.toJSONString(new HashMap<String,Object>(){{
  put("sub", subject);
}});
String payloadBase= new String(Base64.getEncoder().encode(payload.getBytes()));
SecretKeySpec secretKey = new SecretKeySpec(clientSecret.getBytes(), "HMACSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(secretKey);
byte[] hmacData = mac.doFinal(String.join(".",headerBase,payloadBase).getBytes());
String signature= new String(Base64.getEncoder().encode(hmacData));
String jwt = String.join(".", headerBase, payloadBase, signature);
