# Create a Square Thumbnail or Favicon from Image

Create a square thumbnail or favicon using ImageMagick

Resize `file.png` to a 32x32 px image. Use a value other than 32 to create other icon sizes (e.g. 16x16 or 32x32). Combine two favicon sizes using: `convert icon-16px.png icon-32px.png favicon.ico` For a social media preview image, use `2:1#` for the extent and `1200` for the scale.

`# convert file.png -background transparent -gravity Center -extent 1:1# -scale 32 file-32px.png`


#macos/dotfiles