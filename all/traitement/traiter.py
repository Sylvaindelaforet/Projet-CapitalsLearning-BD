# utiliser imagehash i guess
import imagehash






# # Inspired from https://github.com/JohannesBuchner/imagehash repository
# import imagehash
# from PIL import Image

# def alpharemover(image):
#     if image.mode != 'RGBA':
#         return image
#     canvas = Image.new('RGBA', image.size, (255,255,255,255))
#     canvas.paste(image, mask=image)
#     return canvas.convert('RGB')

# def with_ztransform_preprocess(hashfunc, hash_size=8):
#     def function(path):
#         image = alpharemover(Image.open(path))
#         image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
#         data = image.getdata()
#         quantiles = np.arange(100)
#         quantiles_values = np.percentile(data, quantiles)
#         zdata = (np.interp(data, quantiles_values, quantiles) / 100 * 255).astype(np.uint8)
#         image.putdata(zdata)
#         return hashfunc(image)
#     return function
  
# dhash_z_transformed = with_ztransform_preprocess(imagehash.dhash, hash_size = 8)