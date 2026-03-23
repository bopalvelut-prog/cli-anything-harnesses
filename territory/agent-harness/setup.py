from setuptools import setup
setup(
    name='cli-anything-territory',
    version='1.0.0',
    packages=['cli_anything.territory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-territory=cli_anything.territory:cli']},
)
