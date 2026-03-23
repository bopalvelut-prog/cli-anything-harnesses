from setuptools import setup
setup(
    name='cli-anything-addthis',
    version='1.0.0',
    packages=['cli_anything.addthis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-addthis=cli_anything.addthis:cli']},
)
