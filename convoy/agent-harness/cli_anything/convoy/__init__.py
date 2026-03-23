import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('convoy running')
@cli.command()
def start(): click.echo('convoy started')
if __name__ == '__main__': cli()
