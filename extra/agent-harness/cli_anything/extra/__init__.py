import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('extra running')
@cli.command()
def start(): click.echo('extra started')
if __name__ == '__main__': cli()
