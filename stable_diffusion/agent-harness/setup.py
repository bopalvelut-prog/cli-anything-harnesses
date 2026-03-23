from setuptools import setup
setup(
    name='cli-anything-stable_diffusion',
    version='1.0.0',
    packages=['cli_anything.stable_diffusion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stable_diffusion=cli_anything.stable_diffusion:cli']},
)
