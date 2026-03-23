import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whose running')
@cli.command()
def start(): click.echo('whose started')
if __name__ == '__main__': cli()
