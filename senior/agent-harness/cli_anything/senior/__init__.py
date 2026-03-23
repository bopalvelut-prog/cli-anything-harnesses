import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('senior running')
@cli.command()
def start(): click.echo('senior started')
if __name__ == '__main__': cli()
