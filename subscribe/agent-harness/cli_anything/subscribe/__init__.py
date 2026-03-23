import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('subscribe running')
@cli.command()
def start(): click.echo('subscribe started')
if __name__ == '__main__': cli()
