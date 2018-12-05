#### opencv dependencies
[harfbuzz,a text shaping library.](https://github.com/harfbuzz/harfbuzz)  
[opencv](https://github.com/opencv/opencv)  
[opencv_contrib](https://github.com/opencv/opencv_contrib)  
if you want to write code as below,you should build cv2 by yourself.
```python
ft = cv2.freetype.createFreeType2()
    ft.loadFontData(os.path.join("fonts", 'MS_Mincho.ttf'), id=0)
    if len(boxes)==0:
        print('len=0')

        ft.putText(img=img,
                   text='no result',
                   org=(5,5),
                   fontHeight=fontHeight,
                   color=color,
                   thickness=-1,
                   line_type=cv2.LINE_AA,
                   bottomLeftOrigin=True)

        cv2.imwrite(os.path.join(opt.resultPath, base_name), img)
```
