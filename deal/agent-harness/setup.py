from setuptools import setup
setup(
    name='cli-anything-deal',
    version='1.0.0',
    packages=['cli_anything.deal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deal=cli_anything.deal:cli']},
)
