from jejik import daemon
import subprocess
import os
import sys
import signal
import time


class MinecraftDaemon(daemon):
    def __init__(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        print(root_dir)
        daemon_pidfile = os.path.join(root_dir, "daemon.pid")
        self.server_pidfile = os.path.join(root_dir, "server.pid")
        print(daemon_pidfile)
        print(self.server_pidfile)
        super().__init__(daemon_pidfile)

    def stop(self):
        try:
            with open(self.server_pidfile, 'r') as pf:
                minecraft_pid = int(pf.read().strip())
        except IOError:
            minecraft_pid = None

        try:
            if minecraft_pid is not None:
                os.kill(minecraft_pid, signal.SIGINT)

            time.sleep(1)

            try:
                os.kill(minecraft_pid, 0)  # SIGNULL
                sys.stderr.write("Minecraft process did not terminate after a second.".format(self.pidfile))
            except ProcessLookupError:
                pass
        except ProcessLookupError:
            pass
        super().stop()

    def run(self):
        pid = str(os.getpid())
        with open(self.server_pidfile, 'w+') as f:
            f.write(pid + '\n')

        subprocess.Popen(["java", "-Xms1G", "-Xmx1G", "-jar", "minecraft_server.jar", "nogui"])

if __name__ == "__main__":
        daemon = MinecraftDaemon()
        if len(sys.argv) < 2:
                print("Not enough arguments supplied. Try [start|stop|restart|nod]")
                sys.exit(128)
        if sys.argv[1] == 'start':
                daemon.start()
        elif sys.argv[1] == 'stop':
                daemon.stop()
        elif sys.argv[1] == 'restart':
                daemon.restart()
        elif sys.argv[1] == 'nod':
                daemon.run()
        else:
                print("Unknown command")
                sys.exit(2)
        sys.exit(0)