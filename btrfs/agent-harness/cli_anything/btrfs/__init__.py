import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['btrfs', 'filesystem', 'usage', '/'])
@cli.command()
def balance(): subprocess.run(['btrfs', 'balance', 'start', '/'])
if __name__ == '__main__': cli()
