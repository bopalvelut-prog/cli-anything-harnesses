from setuptools import setup
setup(
    name='cli-anything-ffmpeg_convert',
    version='1.0.0',
    packages=['cli_anything.ffmpeg_convert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ffmpeg_convert=cli_anything.ffmpeg_convert:cli']},
)
