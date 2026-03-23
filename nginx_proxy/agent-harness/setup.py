from setuptools import setup
setup(
    name='cli-anything-nginx_proxy',
    version='1.0.0',
    packages=['cli_anything.nginx_proxy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nginx_proxy=cli_anything.nginx_proxy:cli']},
)
