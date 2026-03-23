from setuptools import setup
setup(
    name='cli-anything-hetzner_price',
    version='1.0.0',
    packages=['cli_anything.hetzner_price'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_price=cli_anything.hetzner_price:cli']},
)
