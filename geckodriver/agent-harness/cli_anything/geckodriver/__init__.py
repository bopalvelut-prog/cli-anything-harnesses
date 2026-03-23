import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1650 running')
@cli.command()
def start(): click.echo('app_1650 started')
if __name__ == '__main__': cli()
