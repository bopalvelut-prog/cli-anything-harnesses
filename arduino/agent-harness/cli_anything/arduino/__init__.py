import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1531 running')
@cli.command()
def start(): click.echo('app_1531 started')
if __name__ == '__main__': cli()
