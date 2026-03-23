import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('structure running')
@cli.command()
def start(): click.echo('structure started')
if __name__ == '__main__': cli()
