# ~Combine multiple images into a video using ffmpeg~

Combine multiple images into a video using ffmpeg

`$ ffmpeg -start_number 0053 -r 1/5 -i IMG_%04d.JPG -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4`



#macos/dotfiles	