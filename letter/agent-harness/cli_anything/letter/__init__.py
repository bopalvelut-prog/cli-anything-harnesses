import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('letter running')
@cli.command()
def start(): click.echo('letter started')
if __name__ == '__main__': cli()
