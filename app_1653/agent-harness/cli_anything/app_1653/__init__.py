import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1653 running')
@cli.command()
def start(): click.echo('app_1653 started')
if __name__ == '__main__': cli()
