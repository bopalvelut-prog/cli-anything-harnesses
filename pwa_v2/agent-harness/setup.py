from setuptools import setup
setup(
    name='cli-anything-pwa_v2',
    version='1.0.0',
    packages=['cli_anything.pwa_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pwa_v2=cli_anything.pwa_v2:cli']},
)
