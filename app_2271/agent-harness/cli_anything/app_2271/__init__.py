import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2271 running')
@cli.command()
def start(): click.echo('app_2271 started')
if __name__ == '__main__': cli()
