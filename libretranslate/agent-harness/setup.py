from setuptools import setup
setup(
    name='cli-anything-libretranslate',
    version='1.0.0',
    packages=['cli_anything.libretranslate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libretranslate=cli_anything.libretranslate:cli']},
)
