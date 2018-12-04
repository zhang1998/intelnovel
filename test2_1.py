backgroud_Image = plt.imread( 'C:\\Users\\daniel\\Desktop\\1.jpg' )
wc = WordCloud ( width = 1024 , height = 768 , background_color = 'white' ,   mask = backgroud_Image , font_path = "C:\\Users\\daniel\\Desktop\\rht.otf" ,   stopwords = sr , max_font_size = 400 ,   random_state = 50 )
wc.generate_from_text ( text )
img_colors =  ImageColorGenerator ( backgroud_Image )
wc . recolor ( color_func = img_colors )
plt . imshow ( wc )
plt . axis ( 'off' )
#不显示坐标轴
plt . show ()
#保存结果到本地
wc . to_file ( 'php.jpg' )
