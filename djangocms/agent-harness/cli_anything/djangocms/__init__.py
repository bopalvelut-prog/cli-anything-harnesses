import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('djangocms running')
@cli.command()
def start(): click.echo('djangocms started')
if __name__ == '__main__': cli()
