import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('comanche running')
@cli.command()
def start(): click.echo('comanche started')
if __name__ == '__main__': cli()
