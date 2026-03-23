import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_1539 running')
@cli.command()
def start(): click.echo('app_1539 started')
if __name__ == '__main__': cli()
