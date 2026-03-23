from setuptools import setup
setup(
    name='cli-anything-hetzner_image',
    version='1.0.0',
    packages=['cli_anything.hetzner_image'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_image=cli_anything.hetzner_image:cli']},
)
