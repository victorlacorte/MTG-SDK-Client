from setuptools import setup, find_packages


setup(
    dependency_links=[
        'https://github.com/victorlacorte/MTG-SDK-Client/tree/master#egg=sdk_client',
    ],
    entry_points={
        'console_scripts': [
            # The idea is good bu needs further refinement
            'fetch-cards=sdk_client.scripts.cards_csv:main',
            'fetch-sets=sdk_client.scripts.sets_csv:main',
        ],
    },
    install_requires=[
        'mtgsdk>=1.3.1',
    ],
    name='sdk_client',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    version='0.1',
)
