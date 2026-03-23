import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1615 running')
@cli.command()
def start(): click.echo('app_1615 started')
if __name__ == '__main__': cli()
