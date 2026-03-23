import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lts running')
@cli.command()
def start(): click.echo('lts started')
if __name__ == '__main__': cli()
