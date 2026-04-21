from setuptools import find_packages, setup

description = """SMAC-PettingZoo - Latest StarCraft Multi-Agent Challenge. The origin environment can be found at https://github.com/oxwhirl/smac.git and https://github.com/oxwhirl/smacv2.git."""

setup(
    name="smac_pettingzoo",
    version="1.0.0",
    description="SMAC-PettingZoo - Latest StarCraft Multi-Agent Challenge",
    long_description=description,
    license="MIT License",
    keywords="StarCraft, PettingZoo, Multi-Agent Reinforcement Learning",
    packages=find_packages(),
    install_requires=[
        "protobuf>=6,<8",
        "pys2clientprotocol>=1.0.2",
        "pysc2 @ git+https://github.com/nightly/pysc2.git",
        "absl-py>=0.1.0",
        "numpy>=1.10",
        "pygame>=2.0.0",
        "pettingzoo>=1.24.3",
        "gymnasium",
        "pre-commit",
        "smac @ git+https://github.com/nightly/smac.git",
        "smacv2 @ git+https://github.com/nightly/smacv2.git",
        "loguru",
    ],
)
