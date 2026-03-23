from setuptools import setup
setup(
    name='cli-anything-shop',
    version='1.0.0',
    packages=['cli_anything.shop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shop=cli_anything.shop:cli']},
)
