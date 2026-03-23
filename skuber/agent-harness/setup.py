from setuptools import setup
setup(
    name='cli-anything-skuber',
    version='1.0.0',
    packages=['cli_anything.skuber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skuber=cli_anything.skuber:cli']},
)
