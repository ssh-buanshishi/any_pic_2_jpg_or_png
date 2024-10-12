# 默认配置文件内容
default_config_content = \
"""
[window_pop_behavior] # 【弹窗行为管理】分区标志，勿删！

# 1.【弹窗总开关】
#
# 大多数情况下程序内的弹窗提醒（包括快捷打开日志和配置文件）是需要的，
# 但是如果是用命令行调用此程序（n行命令的那种），进行大批量处理的情况下，
# 可能需要关闭弹窗。因为弹窗的出现会阻塞进程，
# 导致下面的工作运行不了，直接暂停在那，
# 所以这里设置这个选项，可以设置为“关”来一键关闭所有弹窗。
#
# 不过错误信息依旧会输出在终端（cmd黑窗），而且任何时候出了错，
# 错误信息总是会显示在终端，不会因为某个设置而改变
#
# ★★★ 特别注意，由于此设置保存在ini中，而程序一开始创建日志文件，
#       以及之后读取此配置文件时，也有可能引发关键错误，
#       此时由于配置尚未读取解析，还处于默认状态，
#       所以如果不借助配置文件之外的手段，依旧会弹窗。
#       所以这边额外设置了一个特定的【系统环境变量】，通过读取它，
#       来实现：在大部分可能发生错误的操作之前，就能读取到此设置。
#
#       环境变量名为：any_pic_2_pop_window_main_switch（大小写随意）
#
#       环境变量的值对应的含义和选项，与这里的配置文件相同，
#       且★★ 优先级高于此配置文件 ★★，
#       也就是说，如果在环境变量里得到了设置，配置文件将会被跳过。
#
# 开：'1', 'yes', 'true', 'on' （大小写随意，下面有相似的“是/否”选项，同样适用）
# 关：'0', 'no', 'false', 'off'（大小写随意，下面有相似的“是/否”选项，同样适用）

pop_window_main_switch = 1



# 2.【单纯双击启动程序“any_pic_2_jpg.exe” / “to_jpg.bat”，
#    没有路径传入时，此程序对应的表现】
#
# 非负整数，可取值：0 | 1 | 2 | 3 | 4 | 5
#
# 1：弹窗提示后，打开配置文件 ⇨ 【配置.ini】供修改编辑。（新手提示）
#
# 2：不弹窗，直接打开配置文件 ⇨ 【配置.ini】供修改编辑。（熟悉后可改为这个）
#
# 3：弹窗提示后，打开运行日志 ⇨ 【运行日志.log】供查看（如果有的话）。      （3～6是补充备用的快捷方式）
#    
# 4：不弹窗，直接打开运行日志 ⇨ 【运行日志.log】供查看（如果有的话）。
#
# 5：弹窗提示后，打开【软件所在目录】。
#
# 6：不弹窗，直接打开【软件所在目录】。
#
#
#
# 7：仅弹窗提醒，但不打开配置文件【配置.ini】、【运行日志.log】和【软件所在目录】其中任何一个。
#
# 0：不弹窗，也不打开配置文件【配置.ini】和【运行日志.log】其中任何一个，
#    只在cmd终端留下“无路径传入”的提示。

to_jpg_exe_no_path_parameter_behavior = 1



# 3.【单纯双击启动程序“any_pic_2_png.exe” / “to_png.bat”，
#    没有路径传入时，此程序对应的表现】
#
# 非负整数，可取值：0 | 1 | 2 | 3 | 4 | 5
#
# 1：弹窗提示后，打开配置文件 ⇨ 【配置.ini】供修改编辑。            （1～4是补充备用的快捷方式）
#
# 2：不弹窗，直接打开配置文件 ⇨ 【配置.ini】供修改编辑。
#
# 3：弹窗提示后，打开运行日志 ⇨ 【运行日志.log】供查看（如果有的话）。
#    
# 4：不弹窗，直接打开运行日志 ⇨ 【运行日志.log】供查看（如果有的话）。
#
# 5：弹窗提示后，打开【软件所在目录】。（新手提示）
#
# 6：不弹窗，直接打开【软件所在目录】。（熟悉后可改为这个）
#
#
#
# 7：仅弹窗提醒，但不打开配置文件【配置.ini】、【运行日志.log】和【软件所在目录】其中任何一个。
#
# 0：不弹窗，也不打开配置文件【配置.ini】和【运行日志.log】其中任何一个，
#    只在cmd终端留下“无路径传入”的提示。

to_png_exe_no_path_parameter_behavior = 5



# 4.【打开处理完毕时的弹窗】
#
# 处理完毕时的弹窗，除了默认的“完成”用来退出窗口外，
# 还包含“打开运行日志”和“给作者加鸡腿（打赏）”的功能
#
# 设计这个弹窗的目的是在单次运行结束后，能即时快速查看运行日志（弹窗就在眼前），
# 看看哪些文件出了问题。
# 因为图方便的话，一般只会把两个bat启动器的快捷方式建在桌面，
# 快捷方式建得多了桌面就会乱，上面2条的设置就是为了方便改配置和看日志，
# 不用单独建一个配置文件以及日志文件的快捷方式。
#
# PS：当然，也有我想要打赏的原因 (～￣▽￣)～
# 
# 如果一次性有多条命令、大量批处理，不想被结束弹窗阻塞的情况下，
# 请将此选项设置为“否”
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

show_finish_window = 1



# 5.【打开关键错误弹窗】
#
# 关键错误有：组件丢失、无法创建或合并日志文件、程序多开错误（同一时段只能有一个exe在运行）……
#
# 关于程序多开：
#       “any_pic_2_jpg.exe” / “to_jpg.bat”
#    和 “any_pic_2_png.exe” / “to_png.bat”
#    同一时段只能运行其中一个，且同一时段只能有一个进程处于运行状态
#
# ★★★ 同“1.【弹窗总开关】”，此设置也有其对应的【环境变量名】，
#
#       名字为：any_pic_2_show_critical_error_window（大小写随意）
#
#       环境变量的值对应的含义和选项，与这里的配置文件相同
#       且★★ 优先级高于此配置文件 ★★，
#       也就是说，如果在环境变量里得到了设置，配置文件将会被跳过。
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

show_critical_error_window = 1




[transfer] # 【转移文件的设置】分区标志，勿删！

# 6.【复制策略】
# 输入为文件夹时，其中文件出错或跳过时，复制到输出文件夹的策略
#
# 注：如果命令行传入，或者鼠标拖放的其中一个对象是文件，这个文件被跳过或者出错时，
#        不会有任何新文件产生，所以也就不需要配置这个【复制策略】；
#     但是当其中一个对象是文件夹时，为了保持文件夹结构，方便用户梳理，
#     跳过、排除或者出错的文件都会复制到输出文件夹里，
#     此时就有下面两个复制策略可供选择：
#
#     ★ 硬链接：
#        因为只需要创建一个指向同一文件数据区域的“链接”，
#        所以速度非常快，文件的大小影响不到它的速度，绝大多数情况下是首选；
#        但是如果需要对文件进行编辑的话，就会“牵一发而动全身”，
#        硬链接前后两份“文件”的数据都会同步改变，毕竟指向的是同一个数据区域。
#        这样可能会对不熟悉硬链接特性的用户，产生意想不到的后果。
#     ★ 传统拷贝：
#        将文件的数据复制出来一份到新文件。
#        复制数据需要时间，所需的时间和文件大小成正比，
#        当遇到文件数量多或者文件尺寸大的情况时，速度明显会慢下来不少，
#        但使用传统拷贝，拷贝前后两份文件的数据，是完全独立的，
#        修改其中一个，另一个的数据不会像硬链接那样同时改变。
#        
#        所以要额外增设这一选项，让用户有传统拷贝和硬链接两个选项。
# 
#
# 非负整数，可取值：0|1|2
#     0：默认，先尝试硬链接，不行再拷贝
#     1：只用传统拷贝
#     2：只用硬链接

copy_method = 0






[quality] # 分区标志，勿删！


# 7.【输出的jpg图片质量】
#
# 非零正整数，取值范围：(0-100]，左开右闭（质量为0的jpg我觉得有点危险）

jpg_quality = 98

; pillow文档里推荐的是95，再往上也不是不可以，不过文件大小估计会显著增大，因为会禁用一些压缩算法
; 不过处理速度因此明显变快，我这边测试选取的是98，98比95明显快些
; 需要高质量输出的场景下，可以改为100。
; 说明参见：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-saving



# 8.【jpg子采样选项】
#
# 非负整数，可取值：0|1|2 ，其所代表含义如下所示
#     0：4:4:4
#     1：4:2:2
#     2：4:2:0

jpg_subsample_option = 0

; 这边测试由1到0的尺寸增加不大，为了色彩，推荐选择“0”
; 说明参见：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-saving



# 9.【png无损压缩（zip）的等级】
#
# 非负整数，取值范围：[0-9]，双闭区间
# 压缩前后数据都是无损的，数字越高，zip压缩等级越高，耗时间和CPU越高，
# 注意！数值为0时不压缩，输出的文件非常大！不推荐！

png_compress_level = 1

; 自己测试过，compress_level在0-1变化过程中文件显著变小，0是不压缩的，1是无损急速压缩，
; 数字再往上文件尺寸减少的量级几乎可以忽略，而且速度越来越慢，还不如用1快速，
; 毕竟现在很少在乎这么点图片文件尺寸的大小了，而且还要图片是无损的。
; 说明参见：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png-saving






[format] # 【格式设置】分区标志，勿删！


# 10.【用户自定义排除的格式】
#
# ★此字段可为空★
#
# 图片格式填写的标准请参照 “ 可填写的【用户自定义排除的格式】列表.txt ” ，一长条横杠下面
# 第一行的第一列的就是（AVIF、BLP、BMP……），
# 总之填写的是pillow支持的格式，其他pillow自身不支持的格式由其他排除选项控制
#
# 大小写可随意，程序会自动转换为大写
#
# =====================================================================================
#
#
#
# ★★ 此项设置可排除的对象不包括：
#      RAW格式图片、苹果LIVP动态照片、华为动态照片、PDF、SVG、微信dat加密图片，
#      这几项的排除设置请参见“12.”、“13.”、“15.”、“17.”、“21.”、“23.”
#      排除时，上述对象均视为一个整体来看待，而不是解析后
#      看他们中内嵌的图片（如有的话）来决定是否排除。
#
#      对于上述对象整体中的一部分的排除策略，请看下方。
#
# ★★　（1）RAW格式的图片就是它本身，没有内嵌图片和直接输出的说法，显然只能选择是否转换
#
# 　　　（2）对于苹果LIVP动态照片、华为动态照片：
#           由于它们都是一个图片和一个视频打包在一起，成为一个文件
#           所以此处的排除设置，也适用于LIVP、华为动态照片，
#           这两个【图片+视频】组合打包格式中的那张【图片】，
#           前提是它们各自的直接输出（14.和16.）设置为“否”，
#            如果打开直接输出的话，是不走格式排除和转换格式这个流程，直接输出的。
#
# 　　　（3）此项设置同样适用于PDF中的内嵌图片，前提是“19.【PDF内嵌图片直接输出，不转换】”设置为“否”
#           注：输出【PDF的页面渲染图】是需要根据PDF中文字和图片的位置生成的，
#               所以不存在直接输出（直接导出）一说，
#               导出的页面渲染图的格式完全按照程序自身来的：
#                 (1)“any_pic_2_jpg.exe” / “to_jpg.bat” 输出的是jpg，
#                    输出质量受“7.【输出的jpg图片质量】”和“8.【jpg子采样选项】”控制；
#                 (2)“any_pic_2_png.exe” / “to_png.bat” 输出的是png，
#                    输出质量受“9.【png无损压缩（zip）的等级】”控制。
#
# 　　　（4）对于SVG格式：
#
#           ★★★      本排除列表对SVG无效      ★★★
#
#           由于cairosvg库的限制，SVG经过它处理后，只能转出png图片
#           ---------------------------------------------------------------
#           如果“16.【SVG转换后直接输出PNG】”设置为“是”，
#           或者使用了 “any_pic_2_png.exe” / “to_png.bat” ，
#           都将直接输出cairosvg库转换出的png。
#           ---------------------------------------------------------------
#           只有使用 “any_pic_2_jpg.exe” / “to_jpg.bat” ，
#           且“16.【SVG转换后直接输出PNG】”设置为“否”
#           才会强制转换为jpg文件
#           ---------------------------------------------------------------
#
#           png转png不仅速度慢，也压缩不了多少空间，还不如直接输出；
#           png强制转换为jpg后将丢失透明通道信息。
#           所以综上，“16.【SVG转换后直接输出PNG】”设置为“是”，
#           让svg转出的png直接输出，是上策
#
#
# 　　　（5）此项设置同样适用于微信加密的dat图片，
#           前提是“18.【微信dat图片解密后直接输出，不转换】”设置为“否”
#
#
#
# =====================================================================================
#
#
#
# 可用若干个：“,”、“，”、“、”、“|”、“\”、“/” 进行分割，
# 分隔符两边可以有空格，头尾均可有多余的分隔符
#
#     如: （1）,PNG , BMP,JPEG,
#         （2）PNG || BMP || JPEG ||
#         （3）PNG 、BMP ||| JPEG 、
#     总之自己顺眼即可
#
# 注：程序使用的“re.split()”的匹配式：[\s]*[,|，|、|/|\\\\|\|]+[\s]*




user_defined_excluded_format_set = JPEG , PNG , BMP , ICO ,




; 这边默认排除掉一些常见的、能轻松打开的图像格式：JPEG、PNG
;
; ★★ webp图像到现在兼容性应该很不错了，毕竟是十几年前就有了，
;     但考虑到有些编辑软件对的webp的支持不太行，
;     加上最近我这边用的小红书解析程序解析出的webp图片是jpg后缀的，
;     个人觉得还是得转换。
;     如果确实不需要转换webp的，请在上方的【user_defined_excluded_format_set】里
;     添加“WEBP”
;
; bmp、ico的存在很多时候都有特殊用途，转换它们大多数时候是多此一举，这里就默认不转换
; PSD还是用photoshop来导出比较保险，除非要批量转换，之前也默认排除，
; 但现在引入了专门处理PSD的库，比较有信心些能转出来，所以先去掉了PSD的排除




# 11.【排除已经是目标格式的文件】
#
# 如果输入的文件已经是目标格式，这种情况显然可以不需要强制转换
# 当然想强制转换压缩下大小什么的也是可以的
#
# 注：选择排除的话，运行时将排除：目标格式与“4.【用户自定义排除的格式】”的并集
#     反之，运行时将只排除“4.【用户自定义排除的格式】”
#
# 是：'1', 'yes', 'true', 'on' 
# 否：'0', 'no', 'false', 'off'

exclude_target_format = 1



# 12.【是否转换RAW图片】
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

convert_raw  = 1



# 13.【是否转换苹果LIVP动态照片】
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

convert_livp = 1



# 14.【苹果LIVP动态照片直接输出，不转换】
#
# LIVP（实际上就是zip压缩包）中包含的图片+视频不转换直接输出
#
# 如果选择否，就按通常的流程：
#     先确定图片是否在排除列表里，是否为动画
#     然后再决定是否转换格式
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

livp_direct_output = 0

; 因livp中可能包含heic图片，直接导出后可能无法预览，所以默认不开启



# 15.【是否转换华为动态照片】
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

convert_hwlp = 1



# 16.【华为动态照片直接输出，不转换】
#
# 华为动态照片中包含的图片+视频直接导出，不转换
#
# 如果选择否，就按通常的流程：
#     先确定图片是否在排除列表里，是否为动画
#     然后再决定是否转换格式
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

hwlp_direct_output = 1

; 因为华为动态照片中的图片的格式就是jpg，不需要转换，所以默认开启
; 这样也可以在强制转换压缩jpg时，避开还未导出的华为动态照片



# 17.【是否转换PDF】
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

convert_pdf = 1



# 18.【PDF转换模式】
#
# 非负整数，可取值：0|1|2
#     0：导出嵌入的图片，和PDF所有页面的渲染图
#     1：仅导出嵌入的图片
#     2：仅导出所有页面的渲染图

pdf_mode = 0



# 19.【PDF内嵌图片直接输出，不转换】
#
# PDF中嵌入的图片不转换直接输出
#
# 如果选择否，就按通常的流程：
#     先确定图片是否在排除列表里，是否为动画
#     然后再决定是否转换格式
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

pdf_inside_pic_direct_output = 1



# 20.【PDF页面渲染图缩放比例】
#
# 设置PDF页面渲染图的放大比例
#
# 输入正整数，或正的浮点数（通常也叫小数），最终会转换为浮点数

pdf_page_render_zoom_ratio = 2

; 如果按默认1倍来输出的话，A4大小的可能存在看不清图片上的字的情况
; 所以这边设置为2倍



# 21.【是否转换SVG】
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

convert_svg = 1



# 22.【SVG转换后直接输出PNG】
#
# 因为cairosvg库只给了SVG转换出png的函数，所以如果要输出jpg的话需要额外转换
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

svg_direct_output_png = 1

; 由于svg背景透明的居多，这边建议直接转出png



# 23.【是否转换微信加密的dat图片】
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

convert_wechat_dat = 1



# 24.【微信dat图片解密后直接输出，不转换】
#
# 如果选择否，就按通常的流程：
#     先确定图片是否在排除列表里，是否为动画
#     然后再决定是否转换格式
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

wechat_dat_direct_output = 1






[exif] # 【exif设置】分区标志，勿删！


# 25.【转换时是否保留RAW图片的exif】
#
# 由于使用的rawpy库的限制，pillow接收到的rawpy转换出的矩阵里没有exif信息
# 所以需要额外用exiftool对exif进行转移，转移时间相比不转移，额外要多出1-2秒
#
# 如果不需要raw图片里的exif信息，可设置为“否”，可以加快转换速度，
# 反之，设置为“是”
#
# ★ 注：v1.1版本升级后，调用exiftool转移exif之后的文件是直接输出在stdout，也就是内存中，
#        然后使用程序的预分配写入函数“pre_alloc……”一次性写入磁盘中的，
#        整个转换过程和其他图片一样，也优化到只有一次写出文件的磁盘操作了，
#        所以大可不必担心开启此选项会造成多余的磁盘读写操作。
#
# ★ 仅在需要转换格式时才有效，如果RAW图片格式被排除，原样拷贝时，
#    自然不需要考虑exif转移问题
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

perserve_raw_pic_exif = 0

; 个人理解：
; raw转通用格式，一般都是用于最后把raw文件编辑调色好，准备最后发布的时候使用的，
; 发布出去的图片文件一般不会在意exif信息的保留，所以这边默认设置为不保留



# 26.【转换时是否保留普通图片的exif】
#
# 此项针对的是：除raw图片外的图片，
# 包括：苹果LIVP动态照片、华为动态照片、PDF、SVG、微信dat加密图片
#
# 直接使用pillow自带的exif功能，速度与不保存exif差异不大，默认开启
#
# ★ 仅在需要转换格式时才有效，如果图片格式被排除，最终不输出或者图片原样拷贝时，
#    自然不需要考虑exif转移问题
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

perserve_common_pic_exif = 1



# 27.【转换时是否使用exiftool额外增强保存一次exif】
#
# pillow本身对jpg、png有足够的exif支持，挂上pillow_heif插件后
# 对heic的exif信息支持度也不错，
# 一般只要打开“26.【转换时是否保留普通图片的exif】”就能获取到原图片
# 完整的exif信息并转移到输出的文件里。
#
# 不过exiftool比起来更专业一点，有些pillow对exif支持地不够好的格式exiftool能弥补。
# 所以额外增设这一选项，对需要完整exif信息的用户一个额外的选择，
# 代价是每个图片处理的时间延长1-2秒左右。
#
#
# ★ 注：v1.1版本升级后，调用exiftool转移exif之后的文件是直接输出在stdout，也就是内存中，
#        然后使用程序的预分配写入函数“pre_alloc……”一次性写入磁盘中的，
#        整个转换过程和其他图片一样，也优化到只有一次写出文件的磁盘操作了，
#        所以大可不必担心开启此选项会造成多余的磁盘读写操作。
#
# ★★ 仅在需要转换格式时才有效，如果图片格式被排除，
#      最终不输出、直接输出、图片原样拷贝时，自然不需要考虑exif转移问题
#
# ★★ 此选项对“苹果LIVP动态照片”、“华为动态照片”、“PDF文档”、“微信dat加密图片”
#      以及“RAW图片”无效，原因如下：
#      （1）RAW图片的exif转移本身就用的exiftool，这里如果再来一次就重复了；
#      （2）前4者（“苹果LIVP动态照片”、“华为动态照片”、“PDF文档”、“微信dat加密图片”）
#           的图片格式相对固定且常见，
#           pillow对前4者图片格式的exif支持也不错，
#           没有必要浪费时间再用exiftool转移一次exif。
#           原本程序可以做到：1次读取 + 1次写入 ，就能完成图片的转换，
#           现在因为exiftool只能支持现成的文件路径，所以事先
#           要把这几种格式解包或者解密出【源文件】来，供exiftool使用读取里面的exif信息，
#           而【源文件】只能起到提供信息的作用，并不是最终的输出，所以exif转移完后，
#           还要再删掉【源文件】，
#           程序变麻烦、增加磁盘写入次数和写入量的同时，还增加了出错的几率，
#           所以最终决定不支持对这些格式进行exiftool增强保存exif，
#               如果有强迫症的，建议打开这些格式对应的直接输出功能，
#               这些格式里面内嵌的图片或者解密后的自身都支持直接原样导出，
#               这样就不会有转移exif的烦恼了。
#               或者可以经过一次直接输出过后，对直接输出的文件再运行一次软件，
#               直接输出后，原先的格式已经解包或者解密成单个普通图片了，
#               所以这样就可以支持调用exiftool增强转移exif了。
#
# 是：'1', 'yes', 'true', 'on'
# 否：'0', 'no', 'false', 'off'

exif_enhance = 0



# ====================  ★★ 此项设置 “28.【调用……” 已废弃不用 ★★  ====================

# ★★ 此项设置已废弃不用 ★★
#      废弃原因：v1.1版本升级后的any_pic_2_jpg_or_png利用exiftool自身支持的管道操作，
#               现在支持通过调用exiftool命令行，直接将结果输出到stdout，然后由程序进行捕捉，
#               这样，exiftool写出文件的操作全程都在内存里，
#               最后由“pre_allocate_xxx”函数预分配磁盘空间，
#               一次性从内存直接写出，就不存在磁盘覆写产生的碎片了。

# ---------------  原来的说明和记录：⇩  ---------------
#
# 28.【调用exiftool后，是否整理覆写产生的磁盘碎片】
#
#
#
#
#
# 调用exiftool的场景有：
#     （1）开启了“25.【转换时是否保留RAW图片的exif】”
#     （2）开启了“27.【转换时是否使用exiftool额外增强保存一次exif】”
#
# 非负整数，可取值：0|1|2
#     0：默认，如果为固态就不整理，只有为机械硬盘才整理
#     1：总是整理
#     2：从不整理

# defrag_after_exiftool = 0

; 整理碎片的原理很简单，就是用预分配空间的方式拷贝出一个新的文件
;
; 之所以加这个选项，是因为我用diskgenius查看经过exiftool原地覆写处理过后的文件
; 的数据簇列表，发现一个jpg文件就有56个碎片，这也太夸张了，不得不重视一下
; 固态还好，如果是机械的话，绝对会拖慢速度，
; 毕竟资源管理器通常需要加载一个文件夹下所有图片的预览图。
;
; 默认配置下，程序是用不到exiftool的，此状态下程序无论是转换输出，还是直接拷贝转移，
; 由于都采用了“预分配空间”的一次性连续写入方式（硬链接除外），产生碎片的可能性极小，
; 所以使用默认配置的用户，完全不用担心转换出的文件会产生很多碎片，
; 而且默认配置下没有exiftool的介入，速度会更快

# ---------------  原来的说明和记录：⇧  ---------------








[buffer] # 【缓冲和预分派设置】分区标志，勿删！


# 29.【拷贝文件的内存缓冲区大小】
#
# 拷贝时的读入内存缓冲区的大小
#
# 非零正整数，单位：MiB（MB）

copy_file_buffer_size = 256

; 由于确定拷贝的操作是同磁盘传输，此处效仿FastCopy的同盘拷贝策略
; 先从源文件读一部分数据到内存，然后写入到目标文件，循环往复
; FastCopy给的默认内存缓冲区大小就是 256 MiB
;
; 运行中程序将自动接受或调整缓冲区大小，使之不超过当前剩余可用内存的1/4



# 30.【给临时日志文件预分配的空间】
#
# 非零正整数，单位：MiB（MB）

log_file_allocate_size = 10

; 程序采用：
;     将正在运行的日志先记录到临时日志里，
;     最后和原日志文件一并读入内存，然后将拼接起来的记录覆盖原日志文件的方法，
;     来实现【日期和时间最接近的记录排在最前面】的效果
;
; 给临时日志文件预分配空间同样是为了减少运行时产生的文件碎片
; 因为日志文件采用的行缓冲，用于尽可能记录出错前的信息，
; 所以写入频率很高，产生碎片的几率也比一次性全写入的大
; 所以特地安排了日志文件的预分配
; 预分配 10 MiB 大小应该是绰绰有余了
;
; 合并日志文件时，会自动过滤掉临时日志文件尾部尚未被使用的“00”，这点可以放心
;
; 运行中程序将自动接受或调整预分配空间大小，
; 使之不超过 4*10^9 字节（以10^9个日志字符数限制，一个字符4字节来计算）

"""