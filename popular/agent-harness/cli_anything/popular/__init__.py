import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('popular running')
@cli.command()
def start(): click.echo('popular started')
if __name__ == '__main__': cli()
