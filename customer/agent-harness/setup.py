from setuptools import setup
setup(
    name='cli-anything-customer',
    version='1.0.0',
    packages=['cli_anything.customer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-customer=cli_anything.customer:cli']},
)
