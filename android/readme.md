#### oauth for android
[AppAuth-Android](https://github.com/openid/AppAuth-Android)

#### for test extra para
  public class MainActivity extends AppCompatActivity {
```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Bundle extra= getIntent().getExtras();
        if(extra!=null){
            String accessToken=extra.getString("accessToken");
            Toast.makeText(this, "exiting "+accessToken, Toast.LENGTH_LONG).show();
        }
    }
}
```
