from setuptools import setup, find_packages


setup(
    dependency_links=[
<<<<<<< HEAD
        'https://github.com/victorlacorte/MTG-SDK-Client@dev#egg=src',
=======
        'https://github.com/victorlacorte/MTG-SDK-Client#egg=mtg_sdk_client',
>>>>>>> refs/remotes/origin/master
    ],
    entry_points={
        'console_scripts': [
            'fetch-cards=mtg_sdk_client.scripts.cards_csv:main',
            'fetch-sets=mtg_sdk_client.scripts.sets_csv:main',
        ],
    },
    install_requires=[
        'mtgsdk>=1.3.1',
    ],
    name='mtg_sdk_client',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    version='0.0',
)
