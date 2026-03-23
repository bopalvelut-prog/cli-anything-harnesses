import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('restaurant running')
@cli.command()
def start(): click.echo('restaurant started')
if __name__ == '__main__': cli()
