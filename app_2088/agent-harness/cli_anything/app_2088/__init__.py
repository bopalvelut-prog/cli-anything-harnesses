import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2088 running')
@cli.command()
def start(): click.echo('app_2088 started')
if __name__ == '__main__': cli()
