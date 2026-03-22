import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Tezos node')
@cli.command()
def baker(): click.echo('Tezos baker')
if __name__ == '__main__': cli()
