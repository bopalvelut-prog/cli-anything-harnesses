from setuptools import setup
setup(
    name='cli-anything-pure',
    version='1.0.0',
    packages=['cli_anything.pure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pure=cli_anything.pure:cli']},
)
