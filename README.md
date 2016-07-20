# simple-minecraft-daemon
A quick script I threw together for running our minecraft server in a hacky "daemon"

## Development



## License
Currently using the GNU v3 license for the project. Will need to check what license jejik's daemon uses, currently can't check because as their site appears to be down.

## Installation

Nothing special. Just download the two python files (`main.py` and `jejik.py`) to the directory that has `minecraft_server.jar` in it. `minecraft_server.jar` is downloaded from Mojang, and is just renamed to strip out the version information.

Oh, and ensure that Python 3.x is installed on your system.

## Usage

`python3 main.py start` to start
`python3 main.py restart` to restart
`python3 main.py stop` to stop
`python3 main.py nod` to run the code in a "non daemonised" format. Useful for debugging if the server isn't working properly.

## Disclaimer

Code "as-is". Use at your own risk. Do not expose to bright light. Do not make code damp. Do not feed code after midnight UTC. May contain traces of nut.