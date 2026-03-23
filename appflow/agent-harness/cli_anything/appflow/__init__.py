import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appflow running')
@cli.command()
def start(): click.echo('appflow started')
if __name__ == '__main__': cli()
