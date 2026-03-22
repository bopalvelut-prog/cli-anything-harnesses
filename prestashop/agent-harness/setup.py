from setuptools import setup
setup(
    name='cli-anything-prestashop',
    version='1.0.0',
    packages=['cli_anything.prestashop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prestashop=cli_anything.prestashop:cli']},
)
