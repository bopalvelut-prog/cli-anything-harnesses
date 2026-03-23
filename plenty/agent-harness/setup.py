from setuptools import setup
setup(
    name='cli-anything-plenty',
    version='1.0.0',
    packages=['cli_anything.plenty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plenty=cli_anything.plenty:cli']},
)
