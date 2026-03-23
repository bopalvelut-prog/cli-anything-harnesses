import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recall running')
@cli.command()
def start(): click.echo('recall started')
if __name__ == '__main__': cli()
