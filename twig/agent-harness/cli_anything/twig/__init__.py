import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twig running')
@cli.command()
def start(): click.echo('twig started')
if __name__ == '__main__': cli()
