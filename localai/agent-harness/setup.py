from setuptools import setup
setup(
    name='cli-anything-localai',
    version='1.0.0',
    packages=['cli_anything.localai'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-localai=cli_anything.localai:cli']},
)
