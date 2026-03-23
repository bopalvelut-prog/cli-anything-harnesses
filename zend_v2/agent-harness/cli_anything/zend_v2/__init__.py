import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('app_2240 running')
@cli.command()
def start(): click.echo('app_2240 started')
if __name__ == '__main__': cli()
