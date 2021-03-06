### how to generate JWT
```java
String header=JSON.toJSONString(Collections.singletonMap("alg","HS256"));
String headerBase = new String(Base64.getEncoder().encode(header.getBytes()));
long issueAt=new Date().getTime()/1000;
String payload=JSON.toJSONString(new HashMap<String,Object>(){{
  put("exp", issueAt+7199);
  put("iat", issueAt);
}});
String payloadBase= new String(Base64.getEncoder().encode(payload.getBytes()));
SecretKeySpec secretKey = new SecretKeySpec(clientSecret.getBytes(), "HMACSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(secretKey);
byte[] hmacData = mac.doFinal(String.join(".",headerBase,payloadBase).getBytes());
String signature= new String(Base64.getEncoder().encode(hmacData));
String jwt = String.join(".", headerBase, payloadBase, signature);
```
### how to verify JWT
```java
SignedJWT signedJWT = SignedJWT.parse(jwt);
String[] jwtPart=jwt.split("\\.");
String algo = getJCAAlgorithmName(signedJWT.getHeader().getAlgorithm());
SecretKeySpec sk = new SecretKeySpec(clientSecret.getBytes(), algo);
Mac mac = Mac.getInstance(algo);
mac.init(sk);

String signedContent = String.join(".",jwtPart[0],jwtPart[1]);
mac.update(signedContent.getBytes());
byte[] exp=mac.doFinal();

return ConstantTimeUtils.areEqual(exp, signedJWT.getSignature().decode());
```

[c-sharp-how-to-verify-signature-on-jwt-token](https://stackoverflow.com/questions/38725038/c-sharp-how-to-verify-signature-on-jwt-token)  
[jwt claims](https://www.iana.org/assignments/jwt/jwt.xhtml)
