import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('target running')
@cli.command()
def start(): click.echo('target started')
if __name__ == '__main__': cli()
