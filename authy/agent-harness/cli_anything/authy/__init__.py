import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authy running')
@cli.command()
def start(): click.echo('authy started')
if __name__ == '__main__': cli()
