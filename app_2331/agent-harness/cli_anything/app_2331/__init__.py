import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2331 running')
@cli.command()
def start(): click.echo('app_2331 started')
if __name__ == '__main__': cli()
