import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def build(): subprocess.run(['webpack', '--mode', 'production'])
@cli.command()
def dev(): subprocess.run(['webpack', 'serve', '--mode', 'development'])
@cli.command()
def watch(): subprocess.run(['webpack', '--watch'])
if __name__ == '__main__': cli()
