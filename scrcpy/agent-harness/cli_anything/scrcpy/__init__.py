import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def mirror(): subprocess.run(['scrcpy'])
@cli.command()
def record(): subprocess.run(['scrcpy', '--record', 'screen.mp4'])
@cli.command()
def list(): subprocess.run(['adb', 'devices'])
if __name__ == '__main__': cli()
