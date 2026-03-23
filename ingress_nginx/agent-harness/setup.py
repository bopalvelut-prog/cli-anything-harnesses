from setuptools import setup
setup(
    name='cli-anything-ingress_nginx',
    version='1.0.0',
    packages=['cli_anything.ingress_nginx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ingress_nginx=cli_anything.ingress_nginx:cli']},
)
