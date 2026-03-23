import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('combine running')
@cli.command()
def start(): click.echo('combine started')
if __name__ == '__main__': cli()
