import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def connect(): click.echo('IRC connected')
@cli.command()
def join(): click.echo('IRC channel joined')
if __name__ == '__main__': cli()
