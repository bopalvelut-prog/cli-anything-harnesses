import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dominant running')
@cli.command()
def start(): click.echo('dominant started')
if __name__ == '__main__': cli()
