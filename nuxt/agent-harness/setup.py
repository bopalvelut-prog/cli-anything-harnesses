from setuptools import setup
setup(
    name='cli-anything-nuxt',
    version='1.0.0',
    packages=['cli_anything.nuxt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nuxt=cli_anything.nuxt:cli']},
)
