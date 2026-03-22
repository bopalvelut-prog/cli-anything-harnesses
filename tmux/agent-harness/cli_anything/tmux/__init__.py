import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.option('-s', '--session', default='main')
def new(session): subprocess.run(['tmux', 'new', '-s', session])
@cli.command()
def attach(): subprocess.run(['tmux', 'attach'])
@cli.command()
def sessions(): subprocess.run(['tmux', 'ls'])
@cli.command()
@click.argument('session')
def kill(session): subprocess.run(['tmux', 'kill-session', '-t', session])
if __name__ == '__main__': cli()
