from setuptools import setup
setup(
    name='cli-anything-vimeo',
    version='1.0.0',
    packages=['cli_anything.vimeo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vimeo=cli_anything.vimeo:cli']},
)
