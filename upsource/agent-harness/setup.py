from setuptools import setup
setup(
    name='cli-anything-upsource',
    version='1.0.0',
    packages=['cli_anything.upsource'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-upsource=cli_anything.upsource:cli']},
)
