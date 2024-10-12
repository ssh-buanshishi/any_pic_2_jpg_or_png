import os,sys,io
# 代码注释库
from typing import Union , Optional
## 图像库和插件
from PIL import Image
# 挂在PIL上的jpls(JPEG-LS,JPEG-Lossless)编解码插件（https://pypi.org/project/pillow-jpls/）
import pillow_jpls

# 挂在PIL上的heic、avif编解码插件（https://pypi.org/project/pillow-heif/）
from pillow_heif import register_heif_opener,register_avif_opener
register_heif_opener(
    # 参见：https://pillow-heif.readthedocs.io/en/latest/options.html
    quality=-1,
    thumbnails=False,
    save_to_12bit=True,
    allow_incorrect_headers=True,
)
register_avif_opener(
    # 参见：https://pillow-heif.readthedocs.io/en/latest/options.html
    quality=-1,
    thumbnails=False,
    save_to_12bit=True,
    allow_incorrect_headers=True,
)

# 如果后续有其他Pillow插件的话，请在这里import进来
# import xxxxx



import PIL.features

output_file = "可填写的【用户自定义排除的格式】列表.txt"
try:
    os.remove(output_file)
except:
    pass



with open(output_file , mode="wt" , encoding="utf-8-sig" , errors="replace" , newline="\r\n") as f:
    PIL.features.pilinfo(f)
    f.truncate()
    f.seek(0 , os.SEEK_SET)
    sys.stdout.write(f.read())
    sys.stdout.flush()



print("\n\n获取并导出文本完毕，按任意键结束")
os.system("@pause>nul")
sys.exit(0)
