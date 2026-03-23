import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1741 running')
@cli.command()
def start(): click.echo('app_1741 started')
if __name__ == '__main__': cli()
