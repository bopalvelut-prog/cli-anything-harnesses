import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mystery running')
@cli.command()
def start(): click.echo('mystery started')
if __name__ == '__main__': cli()
