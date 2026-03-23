from setuptools import setup
setup(
    name='cli-anything-ingress',
    version='1.0.0',
    packages=['cli_anything.ingress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ingress=cli_anything.ingress:cli']},
)
