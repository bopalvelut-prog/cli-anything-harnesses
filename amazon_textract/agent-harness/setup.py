from setuptools import setup
setup(
    name='cli-anything-amazon_textract',
    version='1.0.0',
    packages=['cli_anything.amazon_textract'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_textract=cli_anything.amazon_textract:cli']},
)
