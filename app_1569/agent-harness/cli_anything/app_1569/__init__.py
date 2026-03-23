import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1569 running')
@cli.command()
def start(): click.echo('app_1569 started')
if __name__ == '__main__': cli()
