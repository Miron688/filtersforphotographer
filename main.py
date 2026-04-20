import argparse
from PIL import Image, ImageOps, ImageFilter


def get_image_black_white(image):
    new_image_black_white = image.convert("L")
    new_image_black_white.save("new1.jpg")


def get_image_contrast(image):
    new_image_contrast = ImageOps.autocontrast(image, cutoff=5)
    new_image_contrast.save("new2.jpg")


def get_image_blur(image):
    new_image_blur = image.filter(ImageFilter.GaussianBlur(radius=2.4))
    new_image_blur.save("new3.jpg")


def get_image_median(image):
    new_image_median = image.filter(ImageFilter.MedianFilter(size=3))
    new_image_median.save("new4.jpg")


def get_frame_image(image):
    width, height = image.size
    frame_image = image.transform((width+100, height+100), Image.EXTENT, (-10, -10, width + 10, height + 10), Image.BILINEAR)
    frame_image.save("new5.jpg")


def get_sepia_image(image):
    sepia_r = 112
    sepia_g = 66
    sepia_b = 20
    sepia_image = Image.new("RGB", image.size)
    for x in range(image.width):
        for y in range(image.height):
            r,g,b =  image.getpixel((x,y))
            new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
            sepia_r = min(new_r, 225)
            sepia_g = min(new_g, 255)
            sepia_b = min(new_b, 255)
            sepia_image.putpixel((x,y), (sepia_r, sepia_g, sepia_b))
    sepia_image.save("new6.jpg")


def main():
    parser = argparse.ArgumentParser(description= "фото от фотографа")
    parser.add_argument("-f", "--file_name", help="путь к файлу", default="Image/tumblr_aee74eca7431296e26563bf456a2e56e_8e177cb0_1280.jpg")
    parser.add_argument("--filterwb", action="store_true", help="ч/б фильтр")
    parser.add_argument("--filtercontrast", action="store_true", help="контрастный фильтр")
    parser.add_argument("--filterblur", action="store_true", help=" фильтр размытия")
    parser.add_argument("--filtermedian", action="store_true", help="медианный фильтр ")
    parser.add_argument("--filterframe", action="store_true", help=" фильтр рамки")
    parser.add_argument("--filtersepia", action="store_true", help="фильтр сепии")
    args = parser.parse_args()
    image = Image.open(f"{args.file_name}")
    if args.filterwb:
        get_image_black_white(image)
    else:
        print("нет чёрно-белого фильтра")
    if args.filtercontrast:
        get_image_contrast(image)
    else:
        print("нет контрастного фильтра")
    if args.filterblur:
        get_image_blur(image)
    else:
        print("нет фильтра размытия")
    if args.filtermedian:
        get_image_median(image)
    else:
        print("нет медианного фильта")
    if args.filterframe:
        get_frame_image(image)
    else:
        print("нет фильтра рамки")
    if args.filtersepia:
        get_sepia_image(image)
    else:
        print("нет фильтра сеппии")


if __name__ == "__main__":
    main()
