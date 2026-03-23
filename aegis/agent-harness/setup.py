from setuptools import setup
setup(
    name='cli-anything-aegis',
    version='1.0.0',
    packages=['cli_anything.aegis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aegis=cli_anything.aegis:cli']},
)
