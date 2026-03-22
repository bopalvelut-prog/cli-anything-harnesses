from setuptools import setup
setup(
    name='cli-anything-k9s',
    version='1.0.0',
    packages=['cli_anything.k9s'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-k9s=cli_anything.k9s:cli']},
)
