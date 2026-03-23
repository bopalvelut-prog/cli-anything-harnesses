import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('angular_cli running')
@cli.command()
def start(): click.echo('angular_cli started')
if __name__ == '__main__': cli()
