from setuptools import setup
setup(
    name='cli-anything-keycloak',
    version='1.0.0',
    packages=['cli_anything.keycloak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keycloak=cli_anything.keycloak:cli']},
)
