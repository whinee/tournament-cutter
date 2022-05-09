from setuptools import find_packages, setup
setup(
    name="tournament-cutter",
    author="whinee",
    author_email="whinyaan@pm.me",
    version='0.0.0.0-alpha.0',
    description='Process tetris tournament videos',
    long_description='''Process tetris tournament videos and cut them appropriately using FFmpeg..
    For full information, visit https://tc.comms.whinyaan.xyz''',
    long_description_content_type="text/markdown",
    url="https://github.com/whinee/tournament-cutter",
    project_urls={
        'Documentation': 'https://tc.comms.whinyaan.xyz',
        'Source': 'https://github.com/whinee/tournament-cutter',
        'Tracker': 'https://github.com/whinee/tournament-cutter/issues',
    },
    license="MIT",
    keywords='python windows macos linux cli scraper downloader manga python3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=['rich', 'aiofiles', 'arrow', 'bs4', 'click', 'httpx', 'inquirer', 'lxml', 'msgpack', 'patool', 'pyyaml', 'tabulate', 'toml', 'tqdm', 'yachalk', 'yarl'],
    entry_points = {
        'console_scripts': ['tc=tc.cli:cli'],
    },
)