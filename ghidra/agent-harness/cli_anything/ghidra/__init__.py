import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('binary')
def analyze(binary): click.echo(f'Ghidra analyzing {binary}')
if __name__ == '__main__': cli()
