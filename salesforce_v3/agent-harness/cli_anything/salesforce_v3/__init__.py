import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2337 running')
@cli.command()
def start(): click.echo('app_2337 started')
if __name__ == '__main__': cli()
