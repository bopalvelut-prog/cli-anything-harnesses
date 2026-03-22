import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('binary')
def analyze(binary): click.echo(f'IDA analyzing {binary}')
if __name__ == '__main__': cli()
