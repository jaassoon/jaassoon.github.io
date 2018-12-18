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
