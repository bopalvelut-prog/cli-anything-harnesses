from setuptools import setup
setup(
    name='cli-anything-gallery_dl',
    version='1.0.0',
    packages=['cli_anything.gallery_dl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gallery_dl=cli_anything.gallery_dl:cli']},
)
