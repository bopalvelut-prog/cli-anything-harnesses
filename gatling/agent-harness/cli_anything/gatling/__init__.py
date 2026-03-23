import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gatling running')
@cli.command()
def start(): click.echo('gatling started')
if __name__ == '__main__': cli()
