import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('today running')
@cli.command()
def start(): click.echo('today started')
if __name__ == '__main__': cli()
