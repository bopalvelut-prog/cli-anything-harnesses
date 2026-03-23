import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('angularjs running')
@cli.command()
def start(): click.echo('angularjs started')
if __name__ == '__main__': cli()
