import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2046 running')
@cli.command()
def start(): click.echo('app_2046 started')
if __name__ == '__main__': cli()
