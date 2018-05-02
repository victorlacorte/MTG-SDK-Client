from setuptools import setup, find_packages


setup(
    # dependency_links=[
    #     'https://github.com/victorlacorte/MTG-SDK-Client@dev#egg=mtg_sdk_client',
    # ],
    install_requires=[
    ],
    name='mtg_sdk_client',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    version='0.0',
    tests_require=[
        'pytest',
    ],
)
