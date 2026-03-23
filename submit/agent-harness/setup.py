from setuptools import setup
setup(
    name='cli-anything-submit',
    version='1.0.0',
    packages=['cli_anything.submit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-submit=cli_anything.submit:cli']},
)
