from setuptools import setup
setup(
    name='cli-anything-amazon_managedgrafana',
    version='1.0.0',
    packages=['cli_anything.amazon_managedgrafana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_managedgrafana=cli_anything.amazon_managedgrafana:cli']},
)
