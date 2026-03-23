import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('model running')
@cli.command()
def start(): click.echo('model started')
if __name__ == '__main__': cli()
