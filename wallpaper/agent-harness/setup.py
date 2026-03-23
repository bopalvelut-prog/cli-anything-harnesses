from setuptools import setup
setup(
    name='cli-anything-wallpaper',
    version='1.0.0',
    packages=['cli_anything.wallpaper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wallpaper=cli_anything.wallpaper:cli']},
)
