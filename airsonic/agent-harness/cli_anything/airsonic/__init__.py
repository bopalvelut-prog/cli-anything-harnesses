import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('airsonic running')
@cli.command()
def start(): click.echo('airsonic started')
if __name__ == '__main__': cli()
