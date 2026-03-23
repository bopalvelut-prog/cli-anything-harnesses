import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('immediate running')
@cli.command()
def start(): click.echo('immediate started')
if __name__ == '__main__': cli()
