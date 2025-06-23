from PIL import Image

class ImageResizer:
    @staticmethod
    def resize_image(input_path, output_path, width=None, height=None, scale=None, quality=85):

        with Image.open(input_path) as img:
            original_width, original_height = img.size
            if scale:
                new_width = int(original_width * scale)
                new_height = int(original_height * scale)
            elif width and height:
                new_width, new_height = width, height
            elif width:
                ratio = width / original_width
                new_width = width
                new_height = int(original_height * ratio)
            elif height:
                ratio = height / original_height
                new_width = int(original_width * ratio)
                new_height = height
            else:
                raise ValueError("Debe haber al menos un tamaño")
            
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            resized_img.save(output_path, quality=quality)
            return new_width, new_height