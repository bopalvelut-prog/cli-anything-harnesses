import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('promise running')
@cli.command()
def start(): click.echo('promise started')
if __name__ == '__main__': cli()
