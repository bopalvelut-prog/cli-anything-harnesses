from setuptools import setup
setup(
    name='cli-anything-netlify',
    version='1.0.0',
    packages=['cli_anything.netlify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netlify=cli_anything.netlify:cli']},
)
