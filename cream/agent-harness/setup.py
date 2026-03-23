from setuptools import setup
setup(
    name='cli-anything-cream',
    version='1.0.0',
    packages=['cli_anything.cream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cream=cli_anything.cream:cli']},
)
