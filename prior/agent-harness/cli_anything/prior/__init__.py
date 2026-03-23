import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prior running')
@cli.command()
def start(): click.echo('prior started')
if __name__ == '__main__': cli()
