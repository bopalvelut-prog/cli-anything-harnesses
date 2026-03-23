from setuptools import setup
setup(
    name='cli-anything-share',
    version='1.0.0',
    packages=['cli_anything.share'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-share=cli_anything.share:cli']},
)
