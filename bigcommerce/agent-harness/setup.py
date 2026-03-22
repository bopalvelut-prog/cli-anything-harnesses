from setuptools import setup
setup(
    name='cli-anything-bigcommerce',
    version='1.0.0',
    packages=['cli_anything.bigcommerce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bigcommerce=cli_anything.bigcommerce:cli']},
)
