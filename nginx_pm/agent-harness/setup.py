from setuptools import setup
setup(
    name='cli-anything-nginx_pm',
    version='1.0.0',
    packages=['cli_anything.nginx_pm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nginx_pm=cli_anything.nginx_pm:cli']},
)
