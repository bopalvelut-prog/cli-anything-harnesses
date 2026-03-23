from setuptools import setup
setup(
    name='cli-anything-medicine',
    version='1.0.0',
    packages=['cli_anything.medicine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-medicine=cli_anything.medicine:cli']},
)
