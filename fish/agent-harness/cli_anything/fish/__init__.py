import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fish running')
@cli.command()
def start(): click.echo('fish started')
if __name__ == '__main__': cli()
