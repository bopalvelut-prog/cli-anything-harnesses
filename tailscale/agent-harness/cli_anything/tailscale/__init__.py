import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def up(): subprocess.run(['tailscale', 'up'])
@cli.command()
def status(): subprocess.run(['tailscale', 'status'])
@cli.command()
def ping(): subprocess.run(['tailscale', 'ping', 'auto'])
if __name__ == '__main__': cli()
