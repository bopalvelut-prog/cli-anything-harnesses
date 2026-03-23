import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kinetica running')
@cli.command()
def start(): click.echo('kinetica started')
if __name__ == '__main__': cli()
