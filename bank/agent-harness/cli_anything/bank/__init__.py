import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bank running')
@cli.command()
def start(): click.echo('bank started')
if __name__ == '__main__': cli()
