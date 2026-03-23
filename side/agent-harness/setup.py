from setuptools import setup
setup(
    name='cli-anything-side',
    version='1.0.0',
    packages=['cli_anything.side'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-side=cli_anything.side:cli']},
)
