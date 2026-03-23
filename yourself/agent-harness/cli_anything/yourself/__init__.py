import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yourself running')
@cli.command()
def start(): click.echo('yourself started')
if __name__ == '__main__': cli()
