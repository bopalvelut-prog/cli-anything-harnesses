from setuptools import setup
setup(
    name='cli-anything-nginx',
    version='1.0.0',
    packages=['cli_anything.nginx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nginx=cli_anything.nginx:cli']},
)
