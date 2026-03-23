from setuptools import setup
setup(
    name='cli-anything-amazon_datazone',
    version='1.0.0',
    packages=['cli_anything.amazon_datazone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_datazone=cli_anything.amazon_datazone:cli']},
)
