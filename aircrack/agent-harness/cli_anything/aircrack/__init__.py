import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['airmon-ng', 'start', 'wlan0'])
@cli.command()
def scan(): subprocess.run(['airodump-ng', 'wlan0mon'])
@cli.command()
def crack(): subprocess.run(['aircrack-ng', '-w', '/usr/share/wordlists/rockyou.txt', 'capture.cap'])
if __name__ == '__main__': cli()
