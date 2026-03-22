from setuptools import setup
setup(
    name='cli-anything-imagemagick',
    version='1.0.0',
    packages=['cli_anything.imagemagick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-imagemagick=cli_anything.imagemagick:cli']},
)
