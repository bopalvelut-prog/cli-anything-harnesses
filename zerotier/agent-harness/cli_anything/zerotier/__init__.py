import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def join(): subprocess.run(['zerotier-cli', 'join'])
@cli.command()
def status(): subprocess.run(['zerotier-cli', 'info'])
@cli.command()
def peers(): subprocess.run(['zerotier-cli', 'listpeers'])
if __name__ == '__main__': cli()
