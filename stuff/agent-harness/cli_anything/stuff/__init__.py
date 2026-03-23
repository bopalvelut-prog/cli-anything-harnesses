import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stuff running')
@cli.command()
def start(): click.echo('stuff started')
if __name__ == '__main__': cli()
