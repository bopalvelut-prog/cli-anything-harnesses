from setuptools import setup
setup(
    name='cli-anything-devpod',
    version='1.0.0',
    packages=['cli_anything.devpod'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devpod=cli_anything.devpod:cli']},
)
