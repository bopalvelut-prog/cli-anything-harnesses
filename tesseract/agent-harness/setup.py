from setuptools import setup
setup(
    name='cli-anything-tesseract',
    version='1.0.0',
    packages=['cli_anything.tesseract'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tesseract=cli_anything.tesseract:cli']},
)
